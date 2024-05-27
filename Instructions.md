<--Heightmaps-->
NOTE: 
For heightmaps, there can be a issue with the cache when loading a different texture, if you notice yellow and black strips on the terrain instead of the expected texture, delete the paging file in .gazebo: rm -rf ~/.gazebo/paging
You can check cd ~/.gazebo to see if paging folder has been deleted

<--Heightmap with Husky-->
NOTE:
- Use absolute paths for the files in heightmap_world.world
- Too steep of a slope will cause husky to stall (perhaps collision or physics engine issue)
- Check how the spawn for husky works, especially z axis

<--Converting world with gazebo_map_creator-->
cd traversability_analysis_ws_ros2
source install/setup.bash
Terminal 1: (Launch your world file with libgazebo_map_creator.so) eg: gazebo -s libgazebo_map_creator.so /home/charlie/traversability_analysis_ws_ros2/src/husky/husky_gazebo/worlds/heightmap_world.world

After launch world file, there should be these services in ros2 service list
/gazebo/describe_parameters
/gazebo/get_parameter_types
/gazebo/get_parameters
/gazebo/list_parameters
/gazebo/set_parameters
/gazebo/set_parameters_atomically
/world/map_save

Terminal 2: ros2 run gazebo_map_creator request_map.py -c '(-10.0,-10.0,0.03)(10.0,10.0,3.0)' -r 0.03 -f /home/charlie/traversability_analysis_ws_ros2/src/Maps/map
Will generate [.bt .pcd, .pgm, .png, .yaml] files
For reference on parameters for adjustment: https://medium.com/@arshad.mehmood/ros2-gazebo-world-map-generator-a103b510a7e5
/home/charlie/traversability_analysis_ws_ros2/src/Maps/map is the location to save followed by file save name in this case it saves it as map
.bt: octovis XXX.bt (press 1 for heightmap specificity)
.pcd: pcl_viewer XXX.pcd (press 1,2,3,4 for different coloration, 4 is best for height specificity)

<--Launching world with husky and operating with keyboard(1)/starting simulation data collection(2)-->
cd traversability_analysis_ws_ros2
source install/setup.bash
colcon build
Terminal 1: ros2 launch husky_gazebo custom_world.launch.py world_name:='world_name.world'
Terminal 2(1): python3 /home/charlie/traversability_analysis_ws_ros2/src/husky/husky_control/publish_velocity_keyboard.py	
Terminal 2(2): ros2 launch simulation simulation_data_collection.launch.py 'dataset_type:=training' 'number_tries:=50' 'world_name:=worldname'
Terminal 3: ros2 service call /get_entity_state gazebo_msgs/GetEntityState '{name: husky, reference_frame: world}' --> This gets you the service data, this will be subscribed to by a client later to retrieve robot states, used to check if it is working properly.

<--Generating composite meta dataset for training-->
cd traversability_analysis_ws_ros2
source install/setup.bash
colcon build
cd /home/charlie/traversability_analysis_ws_ros2/src/dataset_generation_training/dataset_generation_training
change the dataset_type variable according to type of dataset, either 1 for training or 2 for evaluation
python3 composite_meta_generation.py
composite meta csvs will be stored at the output path, in original code: /home/charlie/traversability_analysis_ws_ros2/src/dataset_generation_training/csv/
ensure that it is done for both training and evaluation datasets

<--Training the model-->
cd traversability_analysis_ws_ros2
source install/setup.bash
colcon build
ros2 launch dataset_generation_training dataset_generation_training.launch.py
model will be saved in output folder

<--Generating the CNN model architecture-->
cd traversability_analysis_ws_ros2
source install/setup.bash
colcon build
cd /home/charlie/traversability_analysis_ws_ros2/src/dataset_generation_training/dataset_generation_training
python3 model_architecture_generation.py
png file will be stored in /home/charlie/traversability_analysis_ws_ros2/src/dataset_generation_training/model_architecture_png

<--Generating traversability map for a specific map-->
cd traversability_analysis_ws_ros2
source install/setup.bash
colcon build
1. Enter evaluation.py in evaluation file under src
2. Replace heightmap_name with name of heightmap with .png
3. Replace sim_hm_max_x, sim_hm_max_y and height_scale_factor with the appropriate values
4. Replace Stride, lower stride = higher resolution
5. Save and compile
6. ros2 launch evaluation evaluation.launch.py
