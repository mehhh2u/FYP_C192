#@misc{Gavrikov2020VisualKeras,
#  author = {Gavrikov, Paul},
#  title = {visualkeras},
#  year = {2020},
#  publisher = {GitHub},
#  journal = {GitHub repository},
#  howpublished = {\url{https://github.com/paulgavrikov/visualkeras}},
#}


import tensorflow as tf
#from tensorflow.keras import models, layers
from tensorflow.keras.models import Sequential, load_model, save_model
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, MaxPooling2D, Conv2D
from tensorflow.keras.regularizers import l2

import visualkeras

from PIL import ImageFont
from collections import defaultdict

patch_size = 60

model = Sequential()
model.add(Conv2D(16, (3, 3), padding = 'valid', input_shape=(patch_size, patch_size, 1), kernel_regularizer=l2(0.001)))  # 32 filters, 3x3 kernel
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))  # Dropout another 25%
model.add(Conv2D(32, (3, 3), kernel_regularizer=l2(0.001)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))  # Dropout 25%
model.add(Conv2D(64, (3, 3), kernel_regularizer=l2(0.001)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))  # Dropout 25%
model.add(Flatten()) 
model.add(Dense(128))  # 128 neurons
model.add(Activation('relu'))
model.add(Dense(2))
model.add(Activation('sigmoid'))
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

color_map = defaultdict(dict)
color_map[Conv2D]['fill'] = 'orange'
color_map[Dropout]['fill'] = 'pink'
color_map[MaxPooling2D]['fill'] = 'red'
color_map[Dense]['fill'] = 'green'
color_map[Flatten]['fill'] = 'grey'



visualkeras.layered_view(model, to_file='/home/charlie/traversability_analysis_ws_ros2/src/dataset_generation_training/model_architecture_png/model_2_architecture.png').show()