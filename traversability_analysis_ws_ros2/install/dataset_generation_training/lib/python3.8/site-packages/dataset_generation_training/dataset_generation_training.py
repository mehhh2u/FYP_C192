#!/usr/bin/env python3

# os
import os

# Warnings
import warnings

# Pandas
import pandas as pd

# Skimage, plotting and sklearn
import skimage
import skimage.io
import skimage.feature
import skimage.transform
import matplotlib.pyplot as plt
import sklearn.metrics

# Numpy
import numpy as np
import math

# Tensorflow
import tensorflow as tf
#from tensorflow.keras import models, layers
from tensorflow.keras.models import Sequential, load_model, save_model
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, MaxPooling2D, Conv2D, ZeroPadding2D
from tensorflow.keras.regularizers import l2
from tensorflow.keras.callbacks import EarlyStopping

# Utility
import time
import json

csv_folder = '/home/charlie/traversability_analysis_ws_ros2/src/dataset_generation_training/csv/'
heightmaps_folder = '/home/charlie/traversability_analysis_ws_ros2/src/dataset_generation_training/heightmaps/'
output_folder = '/home/charlie/traversability_analysis_ws_ros2/src/dataset_generation_training/output/'
training_meta_file = 'meta_training_data.csv'
evaluation_meta_file = 'meta_evaluation_data.csv'

time_window = 50 # Each timeframe is approximately 0.02s, hence 50 timeframes is approximately 1 second

sim_time = 20 # Simulation time

patch_size = 60 # For extracting patches from the heightmap for training, evaluation and testing datasets

advancement_th = 0.10 # A threshhold value in meters used to generate the training dataset.
                      # It determines when a patch is considered 'traversed'

debug = 0 # Debugging level, for more detailed analysis

max_hm_x = 10.0 # Heightmap dimensions for x
max_hm_y = 10.0 # Heightmap dimensions for y

height_scale_factor = 1.0 

warnings.filterwarnings("ignore", category=FutureWarning)

#%% Utility Functions

# Reading an image and adjusting it
def read_image(heightmap_png):
    # reads an image taking into account the scaling and bitdepth
    hm = skimage.io.imread(heightmap_png)
    if hm.ndim > 2: # multiple channels
        hm = skimage.color.rgb2gray(hm)
    elif hm.ndim == 2: # aready in one channel
        # This is generally for images trated in matlab beforehand (one channel + graysca;e + 16bit)
        if hm.dtype == 'uint8':
            divided = 255
        if hm.dtype == 'uint16':
            divided = 65535
        hm = hm/divided
    hm = hm * height_scale_factor # scaled to proper factor (mostly for testing, for training, it is 1.0)
    return hm

# Transform from simulation frame to image frame
def toScreenFrame (s_x, s_y):
    # from simulation frame (gazebo) x right, y up, z out of the screen, center is at the middle of the map
    # to x right , y down, ignoring ; xs,ys need to be multiplied by the image size
    xs = s_x + max_hm_x
    ys = -s_y + max_hm_y
    xs = xs/(max_hm_x-(-max_hm_x))
    ys = ys/(max_hm_y-(-max_hm_y))
    return xs, ys

# Extract heightmap patch
def hmpatch(hm, x, y, alpha, edge, scale = 1):
    # Cut out a patch from the image, centered on (x,y), rotated by alpha
    # degrees (0 means bottom in hm remains in bottom in patch, 90 means bottom in hm becomes right in patch)
    # with a specified edge size (in pixels) and scale (relative)
    tf1 = skimage.transform.SimilarityTransform(translation=[-x, -y])
    tf2 = skimage.transform.SimilarityTransform(rotation=np.deg2rad(alpha))
    tf3 = skimage.transform.SimilarityTransform(scale=scale)
    tf4 = skimage.transform.SimilarityTransform(translation=[+edge/2, +edge/2])
    tf = (tf1 + (tf2 + (tf3 + tf4))).inverse
    corners = tf(np.array([[0,0],[1,0],[1,1],[0,1],[0.5,0.5]])*edge)
    patch = skimage.transform.warp(hm, tf, output_shape=(edge,edge), mode="edge")
    return patch, corners

def hmpatch_only_corners(x, y, alpha, edge, scale = 1):
    # Cut out a patch from the image, centered on (x,y), rotated by alpha
    # degrees (0 means bottom in hm remains in bottom in patch, 90 means bottom in hm becomes right in patch)
    # with a specified edge size (in pixels) and scale (relative)
    tf1 = skimage.transform.SimilarityTransform(translation=[-x, -y])
    tf2 = skimage.transform.SimilarityTransform(rotation=np.deg2rad(alpha))
    tf3 = skimage.transform.SimilarityTransform(scale=scale)
    tf4 = skimage.transform.SimilarityTransform(translation=[+edge/2, +edge/2])    
    tf = (tf1 + (tf2 + (tf3 + tf4))).inverse
    corners = tf(np.array([[0,0],[1,0],[1,1],[0,1],[0.5,0.5]])*edge)
    return corners

# Show the 20 slowest and the 20 fastest patches
def show(sample,hm):
    patch=hmpatch(hm,sample["hm_x"],sample["hm_y"],np.rad2deg(sample["OE_G"]),patch_size,scale=1)[0] # make sure to extract the patch from the correct heightmap
    patch=patch-patch[patch.shape[0]//2,patch.shape[1]//2]
    fig,ax1=plt.subplots(figsize=(7,7))
    ax1.imshow(patch/height_scale_factor,cmap="coolwarm",vmin=-0.1,vmax=+0.1)
    ax1.set_title("advancement: {:.4f}".format(sample["advancement"]))
    plt.show()
    plt.close(fig)

#%% Dataset Generation Functions

def transform_patch(patch):
    t_patch = patch - patch[patch.shape[0]//2, patch.shape[1]//2]
    t_patch = skimage.transform.resize(t_patch, (patch_size, patch_size), mode='constant')
    return t_patch

def generate_single_dataset_cnn(input_csv, heightmap_png):
    hm = read_image(heightmaps_folder + heightmap_png)
    df = pd.read_csv(csv_folder + input_csv).set_index("Time")
    df.columns = df.columns.map(str.strip) # strip spaces
    
    # Convert xy to hm coordinates
    df["hm_x"] = df.apply(lambda r: toScreenFrame(r["CP_X"], r["CP_Y"])[0]*hm.shape[1], axis=1)
    df["hm_y"] = df.apply(lambda r: toScreenFrame(r["CP_X"], r["CP_Y"])[1]*hm.shape[0], axis=1)
    
    # Unit vector of robot orientation
    df["S_oX"] = np.cos(df["OE_G"])
    df["S_oY"] = np.sin(df["OE_G"])
    assert(np.allclose(1,np.linalg.norm(df[["S_oX","S_oY"]],axis=1)))
    
    # dX, dY, distance at 'time_window' timesteps into the future
    dt = time_window
    df["S_dX"] = df.rolling(window=(dt + 1))["CP_X"].apply(lambda x: x.iloc[-1] - x.iloc[0]).shift(-dt)
    df["S_dY"] = df.rolling(window=(dt + 1))["CP_Y"].apply(lambda x: x.iloc[-1] - x.iloc[0]).shift(-dt)
    df["S_d"] = np.linalg.norm(df[["S_dX", "S_dY"]], axis = 1)
    
    # Projecting dX and dY in current direction
    df["advancement"] = np.einsum('ij, if->i', df[["S_dX", "S_dY"]], df[["S_oX", "S_oY"]]) # row dot product
    
    # Setting the label using the threshold value based on advancement
    df["label"] = df["advancement"]>advancement_th
    
    # Filtering the data, skiping the first and last one second, while dropping any N.A values (if any)
    dff = df.loc[df.index>=1].dropna()
    dff = dff.loc[dff.index<=(sim_time - 1)].dropna()
    
    # drop the frams where the robot is upside down (orientation alpha angle [euler's angles]) to avoid false positives
    dff = dff.loc[dff.OE_A>=-2.0].dropna()
    dff = dff.loc[dff.OE_A<=2.0].dropna()
    
    dff = dff.loc[dff.OE_B>=-2.0].dropna()
    dff = dff.loc[dff.OE_B<=2.0].dropna()

    # Plotting Trajectory
    if debug > 0:
        fig,ax=plt.subplots(figsize=(15,15))
        ax.imshow(hm/height_scale_factor, cmap='gray')
        ax.plot(dff["hm_x"], dff["hm_y"], '-y')
        ax.plot(dff["hm_x"].iloc[0], dff["hm_y"].iloc[0], 'oy')
        plt.show()
        
    if debug > 1:
        plt.figure();
        dff.plot.scatter(x = "CP_X", y = "CP_Y")
                
    # Plotting Angles
    if debug > 1:
        plt.figure();
        np.rad2deg(dff["OE_G"]).plot()
        
    if debug > 1:
        plt.figure();
        dff["S_d"].plot()

    # Visualize the data
    if debug >2:
        print("Slow")
        for _, sample in dff.sort_values("advancement").head(20).iterrows():
            show(sample, hm)
            
        print("Fast")
        for _, sample in dff.sort_values("advancement").tail(20).iterrows():
            show(sample, hm)
            
    return dff, hm

def generate_composite_dataset_cnn(meta_csv):
    meta_file = pd.read_csv(csv_folder+meta_csv).set_index("ID")
    meta_dataset = pd.DataFrame()
    heightmaps = dict()
    for _, r in meta_file.iterrows():
        print("Processing: ", r["csv_name"])
        dff, hm = generate_single_dataset_cnn(r["csv_name"], r["heightmap_name"])
        dff["hm"] = r["heightmap_name"]
        meta_dataset = meta_dataset.append(dff)
        if not (r["heightmap_name"]in heightmaps):
            heightmaps[r["heightmap_name"]] = hm
    return meta_dataset, heightmaps

def sample(df, heightmap, sz):
    d = df.sample(1)
    l = d["label"].iloc[0]
    hm = heightmap[d["hm"].iloc[0]]
    patch = hmpatch(hm, d["hm_x"].iloc[0], d["hm_y"].iloc[0], np.rad2deg(d["OE_G"].iloc[0]), patch_size, scale=1)[0]
    patch = transform_patch(patch)
    return patch, l

def make_training_evaluation(df, heightmap, N, sz):
    X = []
    y = []
    for _ in range(N):
        im, l = sample(df, heightmap, sz)
        X.append(im[:, :, np.newaxis])
        y.append(l)
    X = np.array(X).astype('float32')
    y = np.array(y)
    y = tf.keras.utils.to_categorical(y,2)
    return X, y

def generator_tr(df, heightmap, batch_size, sz):
    while True:
        X, y = make_training_evaluation(df, heightmap, batch_size, sz)
        yield (X, y)
        
def generator_ev(df, heightmap, batch_size, sz):
    while True:
        X, y = make_training_evaluation(df, heightmap, batch_size, sz)
        yield (X, y)


#%% Functions for CNN Fitting
class CustomCallbacks(tf.keras.callbacks.Callback): # Create a custom History callback
    
    def __init__(self,validation_data=None,batch_size=150):
        super().__init__()
        self.validation_data = validation_data
        self.batch_size = batch_size
    
    def on_train_begin(self, logs=None):
        self.aucs = []
        self.losses = []
        if 'metrics' not in self.params:
            self.params['metrics'] = []  # Initialize the 'metrics' key if it does not exist
        if 'val_auc' not in self.params['metrics']:
            self.params['metrics'].append('val_auc')  # Append 'val_auc' only if it's not already there

    
    def on_train_end(self, logs={}):
        return
    
    def on_epoch_begin(self, epochs, logs={}):
        return

    def on_epoch_end(self, epoch, logs={}):
        self.losses.append(logs.get('loss'))
        if self.validation_data:
            y_pred = self.model.predict(self.validation_data[0])
            auc_epoch = sklearn.metrics.roc_auc_score(self.validation_data[1], y_pred)
            logs['val_auc'] = auc_epoch
            self.aucs.append(auc_epoch)
            print("auc_epoch appended")
        else:
            print("Validation data not available.")
                
    def on_batch_begin(self, batch, logs={}):
        return
    
    def on_batch_end(self, batch, logs={}):
        return    



#%% Generating datasets for training/evaluation

dataset_training, heightmaps_training = generate_composite_dataset_cnn(training_meta_file)
dataset_evaluation, heightmaps_evaluation = generate_composite_dataset_cnn(evaluation_meta_file)

print("length of training dataset: ", len(dataset_training))
print("length of evaluation dataset: ", len(dataset_evaluation))

dataset_training.to_csv("dataset_training")
dataset_evaluation.to_csv("dataset_evaluation")

#%% Selecting subset of the evaluation dataset for evaluation

X_te, y_te = make_training_evaluation(dataset_evaluation, heightmaps_evaluation, len(dataset_evaluation)//8, patch_size)



np.save("X_te", X_te)
np.save("y_te", y_te)

custom_callbacks = CustomCallbacks(validation_data=(X_te, y_te))
#%% CNN architecture and training
# CNN architecture

# Model 2 acc 75
model = Sequential()
model.add(Conv2D(16, (5, 5), padding = 'valid', input_shape=(patch_size, patch_size, 1), kernel_regularizer=l2(0.001)))  # 32 filters, 3x3 kernel
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.30))  # Dropout 30%
model.add(Conv2D(32, (5, 5), kernel_regularizer=l2(0.001)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.30))  # Dropout 30%
model.add(Conv2D(64, (3, 3), kernel_regularizer=l2(0.001)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.50))  # Dropout 50%
model.add(Flatten())
model.add(Dense(64))  # 64 neurons
model.add(Activation('relu'))
model.add(Dense(128))  # 128 neurons
model.add(Activation('relu'))
model.add(Dense(2))
model.add(Activation('sigmoid'))

# Set the initial learning rate
initial_learning_rate = 0.01

# Define the learning rate schedule
lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate=initial_learning_rate,
    decay_steps=100000,
    decay_rate=0.96,
    staircase=True)

# Create an optimizer with the learning rate schedule
optimizer = tf.keras.optimizers.Adam(learning_rate=lr_schedule)

model.compile(loss='binary_crossentropy',
              optimizer=optimizer,
              metrics=['accuracy'])

#loss='categorical_crossentropy',

# CNN training
batch_size = 200
steps_per_epoch = int(len(dataset_training)//(20*batch_size))
history = model.fit(generator_tr(dataset_training, heightmaps_training, batch_size, patch_size),
                    steps_per_epoch=steps_per_epoch,
                    epochs=20,
                    verbose=2   ,
                    validation_data=(X_te,y_te),
                    callbacks=[custom_callbacks, 
                               tf.keras.callbacks.TensorBoard(log_dir='./logs/'+time.strftime("%Y%m%d%H%M%S"), 
                                                                            histogram_freq=0, 
                                                                            write_graph=False, 
                                                                            write_images=False),
                               tf.keras.callbacks.EarlyStopping(monitor='val_accuracy',
                                                                patience=5,
                                                                restore_best_weights=True)]
                    )

# Save the model
model.save(output_folder+"traversability_husky_b150_spe_50_e_10_patch_60_acc_XX.keras")
model.summary()

# Save the training history
history_filename = output_folder + "traversability_husky_b150_spe_50_e_10_patch_60_acc_XX_history.json"
with open(history_filename, 'w') as f:
    json.dump(history.history, f)
    