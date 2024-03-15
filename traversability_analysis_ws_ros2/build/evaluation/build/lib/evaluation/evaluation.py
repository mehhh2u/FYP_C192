#!/usr/bin/env python3
# os
import os

# Warnings
import warnings

# Pandas
import pandas as pd

# Numpy
import numpy as np

# Skimage
import skimage
import skimage.io
import skimage.filters
import skimage.draw
import skimage.transform
from   skimage import img_as_ubyte

# Plotting
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from   matplotlib import collections as mc

# Tensorflow
import tensorflow as tf

# Networkx
import networkx as nx

# Multiprocessing
from   joblib import Parallel, delayed

# Utility
import time
import math
import json

input_folder = '/home/charlie/traversability_analysis_ws_ros2/src/evaluation/input/'
output_folder = '/home/charlie/traversability_analysis_ws_ros2/src/evaluation/output/'
map_directory = output_folder + "heightmaps_prepped/cost_maps/"
model_folder = input_folder + "model/"
model_name = "traversability_husky_b150_spe_50_e_10_patch_60_acc_78.keras"
heightmaps_folder = input_folder + "heightmaps/"
heightmap_name = "sullens.png"

sim_hm_mx_x = 10.0 # heightmap dimensions (m) used in the simulation for generating training data
sim_hm_mx_y = 10.0 # passes simulation coodrinates to screen coordinates, world is 20mx20m, hence -10 to 10
height_scale_factor = 1.0 # for learning, it was 0 - 1.0, if the heightmap is higher/lower, this should be adjusted by the same degree
stride = 3 # determines 'resolution' of resultant heightmap, lower stride  =  higher resolution, but takes exponentially longer to process
           # this value is dependent on the resolution of the original png file, the larger the resolution and smaller the stride, the longer the process

padding = True # False: Not adding padding to image before processing
               # True: Adding padding to image before processing
               # Helps to prevent image cropping by half the size of the patch size, but results in a affected prediction for the edges

# For multiprocessing, set it to True
multiprocessing = False
multiprocessing_hm = np.zeros((100,100))

warnings.filterwarnings("ignore", category=FutureWarning)

#%% Utility Functions

# Reading an image and adjusting it
def read_image(heightmap_png):
    # reads an image taking into account the scaling and bitdepth
    hm = skimage.io.imread(heightmap_png)
    if hm.ndim == 3:  # Image has multiple channels
        if hm.shape[2] == 3:  # RGB image
            hm = skimage.color.rgb2gray(hm)
        elif hm.shape[2] == 4:  # RGBA image, discard the alpha channel before converting
            hm = skimage.color.rgb2gray(hm[:, :, :3])
        elif hm.shape[2] == 2:  # Not standard, handling as a special case
            # You might handle this case specifically or raise an error
            raise ValueError("Unexpected image format with 2 channels.")
    elif hm.ndim == 2:  # Already in one channel
        # This is generally for images treated in matlab beforehand (one channel + grayscale + 16bit)
        if hm.dtype == 'uint8':
            divisor = 255
        elif hm.dtype == 'uint16':
            divisor = 65535
        else:
            raise ValueError("Unexpected image data type.")
        hm = hm / divisor
    else:
        raise ValueError("Unexpected image dimensions.")
    
    hm = hm * height_scale_factor  # scaled to proper factor (mostly for testing, for training, it is 1.0)
    return hm

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

def transform_patch(patch, sz):
    t_patch = patch - patch[patch.shape[0]//2, patch.shape[1]//2]
    t_patch = skimage.transform.resize(t_patch, (sz, sz), mode='constant')
    return t_patch

def testing_fitted_model(model, heightmap_png, edges, resize, radian_ori, stride, padding):
    print ("Generating traversability image for orientation " + str(radian_ori) + " rads")
    hm = read_image(heightmap_png)
    
    # Adding padding to the heightmap to prevent cropping of the edges due to convolutional behaviours
    if padding:
        pad_width = edges//2
        pad = ((pad_width, pad_width), (pad_width, pad_width))
        # Calculating average pixel value of four corners for padding
        #coordinates = [(0,0), (hm.shape[0]-1, 0), (0, hm.shape[1]-1), (hm.shape[0]-1, hm.shape[1]-1)]
        #pixel_values = [hm[x, y] for x, y in coordinates]
        #average_pixel_value = np.mean(pixel_values)
        #hm = np.pad(hm, pad, mode='constant', constant_values = average_pixel_value)
        hm = np.pad(hm, pad, mode='edge')
        
    X_mp = []
    hm_columns = int((np.shape(hm)[0] - edges) / stride)
    hm_rows = int((np.shape(hm)[1] - edges) / stride)
    
    data = pd.DataFrame()
    data ["patch"] = range(0,hm_columns*hm_rows)
    data.set_index("patch")
    print(f"Patches to be filled up (by {stride})")
    data ["hm_x"] = [int((edges/2) + (j*stride)) for _ in range(0, hm_rows) for j in range(0, hm_columns)]
    data ["hm_y"] = [int((edges/2) + (i*stride)) for i in range(0, hm_rows) for _ in range(0, hm_columns)]
    data ["G"] = [radian_ori for _ in range (0, hm_columns*hm_rows)]
    
    total_samples = len(data.index)
    
    s_Time = time.time()
    print("Cropping patches and extracting features")
    counter = 0
    if multiprocessing == False:
        for i, d in data.iterrows():
            print("\rProcessing " + str(i) + "/" +str(total_samples), end='')
            patch = hmpatch(hm, d["hm_x"], d["hm_y"], np.rad2deg(d["G"]), edges, scale = 1)[0]
            patch = transform_patch(patch,resize)
            X_mp.append(patch[:,:,np.newaxis])
            counter = counter + 1
        print("\rProcessed " + str(counter) + "/" + str(total_samples))
    else:
        print ("\rProcessing " + str(total_samples) + " [multiprocessing]", end='')
        multiprocessing_hm = read_image(heightmap_png)
        X_mp = Parallel(n_jobs=4)
    e_Time = time.time()
    
    elapsed_Time = e_Time - s_Time
    print("-- time: " + str(elapsed_Time))
    print("Estimating traversability for all patches")
    
    s2_Time = time.time()
    
    X = np.array(X_mp).astype('float32')
    y_pred = model.predict(X)
    
    e2_Time = time.time()
    elapsed2_Time = e2_Time - s2_Time
    print("-- time: " + str(elapsed2_Time))
    fig,ax1 = plt.subplots(figsize=(9,9))
    ax1.imshow(hm/height_scale_factor, cmap="viridis")
    fig.savefig(output_folder+ "heightmaps_prepped/" + heightmap_name[:-4] + '_out_viridis_base' + '.png', dpi=fig.dpi)
    
    cax1 = ax1.imshow(hm/height_scale_factor,cmap="viridis")
    cbar = fig.colorbar(cax1, ticks=[round(np.amin(hm)+.01,2), round(np.amax(hm),2)])
    fig.savefig(output_folder+ "heightmaps_prepped/" + heightmap_name[:-4] + '_out_viridis__bar_base' + '.png', dpi=fig.dpi)
    
    fig,ax1=plt.subplots(figsize=(9,9))
    ax1.imshow(hm/height_scale_factor, cmap="gray")
    fig.savefig(output_folder+ "heightmaps_prepped/" + heightmap_name[:-4] + '_out_gray_base' + '.png', dpi=fig.dpi)
    
    # Using a white skimage to draw traversability results
    
    sk_hm = np.ones((np.shape(hm)[0], np.shape(hm)[1], 4),dtype='float64')
    sk_hm [:,:,3] = np.zeros((np.shape(hm)[0], np.shape(hm)[1]),dtype='float64') # Sets alpha channel to zero for the entire image, making it transparent
    
    print("Drawing prdictions on patches for current orientation")
    s3_Time = time.time()
    
    tf = skimage.transform.SimilarityTransform(translation=[edges//2,edges//2], rotation=-radian_ori)
    tf_sk = skimage.transform.SimilarityTransform(translation=[10,10], rotation=-radian_ori)
    arrow_points = tf(np.array([[0, 0], [edges/2, 0]]))
    arrow_points_sk = tf_sk(np.array([[-5, 0], [-10, 5], [5, 0], [-10, -5]])) 
    
    ax1.arrow(arrow_points[0][0],arrow_points[0][1],arrow_points[1][0]-arrow_points[0][0],arrow_points[1][1]-arrow_points[0][1], length_includes_head = True, width=3)
    
    for i,d in data.iterrows():
        print("\rProcessing " + str(i) + "/" + str(total_samples), end='')
        corners = hmpatch_only_corners(d["hm_x"], d["hm_y"], np.rad2deg(d["G"]), stride, scale=1)
        color_box_sk = [0.0,1.0,0.0,y_pred[i][1]] # Green with probability of non-traversability in alpha
        # if we only want to draw the patch without its orientations, use this (avoids holes between patches)
        s_patch = skimage.draw.polygon([ corners[4,1]-stride/2,  corners[4,1]+stride/2, corners[4,1]+stride/2, corners[4,1]-stride/2, corners[4,1]-stride/2], [ corners[4,0]-stride/2, corners[4,0]-stride/2, corners[4,0]+stride/2, corners[4,0]+stride/2, corners[4,0]-stride/2])
        skimage.draw.set_color(sk_hm, (s_patch[0], s_patch[1]), color_box_sk)
        
    # Removing padding
    if padding:
        sk_hm = sk_hm[pad_width:-pad_width, pad_width:-pad_width]
    
    # for ploting with skimage
    sk_hm_pure = np.copy(sk_hm)
    s_patch = skimage.draw.polygon( arrow_points_sk[[0,1,2,3,0],1], arrow_points_sk[[0,1,2,3,0],0])
    skimage.draw.set_color(sk_hm, (s_patch[0],s_patch[1]), [0.0,0.0,1.0,1.0])
    ax1.imshow(sk_hm)
    
    sk_hm = img_as_ubyte(sk_hm)
    sk_hm_pure = img_as_ubyte(sk_hm_pure)
    
    folder_path = os.path.join(map_directory)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    skimage.io.imsave(map_directory + heightmap_name[:-4] + '_out_' + ("%.3f" % radian_ori) + '.png', sk_hm_pure) # sk_hm_pure if you don't want to save the arrows, sk_hm if you want the arrows
    
    e3_Time = time.time()
    elapsed3_Time = e3_Time - s3_Time
    print("\rProcessed " + str(total_samples) + "/" + str(total_samples))
    print("-- time: " + str(elapsed3_Time))
    #print("Traversability Prediction: " + str(y_pred[:][1]))
    #print("Average Corner Pixel Value: " + str(average_pixel_value))
    return sk_hm_pure # sk_hm_pure if you don't want to save the arrows, sk_hm if you want the arrows


# Load fitted model from tensorflow
model = tf.keras.models.load_model(model_folder + model_name)

# heightmap specifications
heightmap_png = heightmaps_folder + heightmap_name
patch_size = 60
patch_resize = 60
hm = read_image(heightmap_png)

if multiprocessing:
    multiprocessing_hm = read_image(heightmap_png)

# evaluate for a number of orientations, outputs are inside the heightmaps folder (testing)
test_orientations = 32
test_orientations_step = 2*np.pi/test_orientations
for i in range(0, test_orientations):
    temporary_memory = testing_fitted_model(model, heightmap_png, patch_size, patch_resize, i*test_orientations_step, stride, padding)


# Making sure maps are in the correct order
map_files = sorted(os.listdir(map_directory))
# Loading the traversability maps into a list of NumPy arrays
cost_maps = [skimage.io.imread(os.path.join(map_directory, f)) for f in map_files if f.endswith('.png')]
# Stacking the maps to create a 3D array (height, width, orientation)
traversability_stack = np.stack(cost_maps, axis = -1)
# Computing the minimum traversability map
min_traversability_map = np.min(traversability_stack, axis = -1)
# Saving the minimum traversability map
skimage.io.imsave(map_directory + heightmap_name[:-4] + '_out_minumum_traversability_map.png', min_traversability_map)

hm_normalized = hm/np.max(hm)
min_traversability_map_normalized = min_traversability_map/np.max(min_traversability_map)

# Create an overlay image
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(hm_normalized, cmap='gray', interpolation='nearest')
ax.imshow(min_traversability_map_normalized, cmap='hot', alpha=1, interpolation='nearest')  # 'hot' colormap for visibility, adjust alpha as needed
ax.axis('off')  # Hide axes for better visualization
plt.savefig(map_directory + heightmap_name[:-4] + '_overlay.png', bbox_inches='tight', pad_inches=0)
plt.close()




