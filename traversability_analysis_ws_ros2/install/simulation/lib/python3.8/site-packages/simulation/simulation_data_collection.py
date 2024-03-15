#!/usr/bin/env python3

import os
import math
import time
import numpy as np
import pandas as pd
from gazebo_msgs.msg import EntityState, ModelStates
from gazebo_msgs.srv import GetEntityState, SetEntityState
from geometry_msgs.msg import Pose, Twist

import tf_transformations as transformations
import threading

import rclpy
from rclpy.node import Node
from rclpy.duration import Duration

## Constant definitions for training/evaluation map simulations
# In m, heightmaps (in simulation) are assumed 'squared' so min_hm_x is equal to -max_hm_x
max_hm_x = 10
max_hm_y = 10
# Max map height, 0 is the min
max_hm_z = 1
# In pixels, heightmaps (images) are assumed squared, gazebo requires sizes 2^n+1 x 2^n+1
im_hm_x = 513
im_hm_y = 513

# Adjust output folder accordingly
output_folder = "/home/charlie/traversability_analysis_ws_ros2/src/simulation/csv/"

## For gazebo communication
model_name = "husky"
root_relative_entity_name = '' # This is the full model and not only the base_link
fixed_twist = Twist()
fixed_twist.linear.x = 0.3 # in m/s
fixed_twist.linear.y = 0.0
fixed_twist.linear.z = 0.0
fixed_twist.angular.x = 0.0
fixed_twist.angular.y = 0.0
fixed_twist.angular.z = 0.0

sim_duration = Duration(seconds = 20)

def randomly_generate_pose():
    # x,y (z will be fixed as the max_hm_z so that the robot will drop down), gamma as orientation
    rn = np.random.random_sample((3,))
    random_pose = Pose()
    random_pose.position.x = 2 * max_hm_x * rn[0] - max_hm_x
    random_pose.position.y = 2 * max_hm_y * rn[1] - max_hm_y
    random_pose.position.z = max_hm_z * 1.0 # Not spawning at max height z to reduce overtuning chances
    qto = transformations.quaternion_from_euler(0, 0, 2*math.pi * rn[1], axes = 'sxyz')
    random_pose.orientation.x = qto[0]
    random_pose.orientation.y = qto[1]
    random_pose.orientation.z = qto[2]
    random_pose.orientation.w = qto[3]    
    return random_pose

def generate_random_model_state():
    random_pose = randomly_generate_pose()
    model_state = EntityState()
    model_state.name = model_name
    model_state.pose = random_pose
    model_state.twist = fixed_twist
    model_state.reference_frame = root_relative_entity_name
    return model_state

def get_model_state(node, model_name, root_relative_entity_name):
    client = node.create_client(GetEntityState, '/gazebo/get_entity_state')
    if not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().error('Service /gazebo/get_entity_state not available.')
        return None

    try:
        request = GetEntityState.Request()
        request.name = model_name
        request.reference_frame = root_relative_entity_name
        future = client.call_async(request)
        rclpy.spin_until_future_complete(node, future)
        response = future.result()
        return response.state if response.success else None
    except Exception as e:
        node.get_logger().error(f'Service call failed: {str(e)}')
        return None

def set_model_state(node, model_state):
    client = node.create_client(SetEntityState, '/gazebo/set_entity_state')
    
    if not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().error('Service /gazebo/set_entity_state not available.')
        return None
    
    try:
        request = SetEntityState.Request()
        request.state = model_state

        future = client.call_async(request)
        rclpy.spin_until_future_complete(node, future)
        return future.result()
    
    except Exception as e:
        node.get_logger().error('Service call failed: %s' % str(e))
        return False
    
def is_pose_in_map(pose):
    little_offset = 0.1 # to avoid waiting until the robot is really on the edge
    if pose.position.x > max_hm_x - little_offset or pose.position.x < -max_hm_x + little_offset:
        return False
    if pose.position.y > max_hm_y - little_offset or pose.position.y < -max_hm_y + little_offset:
        return False
    if pose.position.z < 0.1: # Spawning husky in empty world, the z position pose is z=0.13227300333847308, adjusted accordingly, test for more verification
        return False
    return True

def toScreenFrame (s_x, s_y, s_z):
    # from simulation frame (gazebo) x right, y up, z out of the screen, center is at the middle of the map
    # to x right , y down, ignoring ; xs,ys need to be multiplied by the image size
    xs = s_x + max_hm_x
    ys = -s_y + max_hm_y
    xs = xs/(max_hm_x-(-max_hm_x))
    ys = ys/(max_hm_y-(-max_hm_y))

    return xs, ys

def is_overturned(orientation_quaternion):
    # Convert quaternion to Euler angles
    euler = transformations.euler_from_quaternion([
        orientation_quaternion.x,
        orientation_quaternion.y,
        orientation_quaternion.z,
        orientation_quaternion.w
    ])

    roll, pitch, _ = euler

    # Define thresholds for roll and pitch to consider the vehicle as overturned
    roll_threshold = math.radians(60)  # 60 degrees
    pitch_threshold = math.radians(60)  # 60 degrees

    return abs(roll) > roll_threshold or abs(pitch) > pitch_threshold


class PubsSubsManager(Node):
    def __init__(self):
        super().__init__('simulation_data_collection')
        
        # Simulation parameters
        self.world_name = self.declare_parameter('world_name', 'default_world').get_parameter_value().string_value
        self.dataset_type = self.declare_parameter('dataset_type', 'training').get_parameter_value().string_value
        self.i_sim = self.declare_parameter('number_tries', 10).get_parameter_value().integer_value
        self.starting_time = self.get_clock().now()
        self.initial_pose = None
        self.latest_model_state = None
        
        # Command parameters
        self.send_cmd_vel = False
        self.cmd_vel_topic = '/husky_velocity_controller/cmd_vel_unstamped'
        
        # Subscriber and Publisher
        self.publisher = self.create_publisher(Twist, self.cmd_vel_topic, 10)
        self.subscriber = self.create_subscription(ModelStates, '/gazebo/model_states', self.model_states_callback, 10)
        
        # Data logging
        self.model_states_data = []
        self.meta_data = []
        
    def set_flag_cmd_vel(self, val):
        self.send_cmd_vel = val
    
    def publish_fixed_twist(self):
        while rclpy.ok():
            if self.send_cmd_vel:
                self.publisher.publish(fixed_twist)
            time.sleep(0.1)
    
    def stop_vehicle(self):
        self.set_flag_cmd_vel(False)
        self.get_logger().info(f"vehicle stopped")

    def start_new_simulation_try(self, world_name, dataset_type, i_sim, initial_pose):
        self.get_logger().info(f"Starting new simulation try: {world_name}, {dataset_type}, {i_sim}")
        self.world_name = world_name
        self.dataset_type = dataset_type
        self.i_sim = i_sim
        self.initial_pose = initial_pose
        self.starting_time = self.get_clock().now()
        self.set_flag_cmd_vel(True) # Start publishing twist messages
    
    def model_states_callback(self, msg):
        # Check if initial_pose is set
        if self.initial_pose is None:
            self.get_logger().error('Initial pose is not set.')
            return
        # Find the index of the model
        try:
            index = msg.name.index(model_name)
        except ValueError:
            # Model name not found in the message
            return
        # Processing Model States data and storing it
        elapsed_time = self.get_clock().now() - self.starting_time
        elapsed_time_sec = round(elapsed_time.nanoseconds / 1e9, 2)
        initial_position_x = self.initial_pose.position.x
        initial_position_y = self.initial_pose.position.y
        initial_position_z = self.initial_pose.position.z
        current_position_x = msg.pose[index].position.x
        current_position_y = msg.pose[index].position.y
        current_position_z = msg.pose[index].position.z
        orientation_euler = transformations.euler_from_quaternion([
                                msg.pose[index].orientation.x,
                                msg.pose[index].orientation.y,
                                msg.pose[index].orientation.z,
                                msg.pose[index].orientation.w],
                                axes = 'sxyz')
        twist_linear_vel_x = msg.twist[index].linear.x
        twist_linear_vel_y = msg.twist[index].linear.y
        twist_linear_vel_z = msg.twist[index].linear.z
        twist_angular_vel_x = msg.twist[index].angular.x
        twist_angular_vel_y = msg.twist[index].angular.y
        twist_angular_vel_z = msg.twist[index].angular.z
        self.latest_model_state = msg.pose[index]
        
        # ii: image initial
        ii_position = toScreenFrame(initial_position_x, initial_position_y, initial_position_z)
        # ic: image current
        ic_position = toScreenFrame(current_position_x, current_position_y, current_position_z)
        
        if is_pose_in_map(msg.pose[index]):
            # Store values as a tuple or list
            self.model_states_data.append((elapsed_time_sec,
                                        ii_position[0] * im_hm_x,
                                        ii_position[1] * im_hm_y,
                                        initial_position_x,
                                        initial_position_y,
                                        initial_position_z,
                                        ic_position[0] * im_hm_x,
                                        ic_position[1] * im_hm_y,
                                        current_position_x,
                                        current_position_y,
                                        current_position_z,
                                        orientation_euler[0],
                                        orientation_euler[1],
                                        orientation_euler[2],
                                        twist_linear_vel_x,
                                        twist_linear_vel_y,
                                        twist_linear_vel_z,
                                        twist_angular_vel_x,
                                        twist_angular_vel_y,
                                        twist_angular_vel_z))
        
    def save_model_states_data_to_csv(self, file_path):
        # Convets the data to a DataFrame and save as CSV
        # IRIP: Imageframe Robot Initial Position (in pixels)
        # IP: Initial Posiition
        # IRCP: Imageframe Robot Current Position (in pixels)
        # CP: Current Position
        # OE: Orientation Eular (A: Alpha, B: Beta, G: Gamma)
        # TLV: Twist Linear Velocity
        # TAV: Twist Angular Velocity

        df = pd.DataFrame(self.model_states_data, columns=['Time',
                                                           'IRIP_X',
                                                           'IRIP_Y',
                                                           'IP_X',
                                                           'IP_Y',
                                                           'IP_Z',
                                                           'IRCP_X',
                                                           'IRCP_Y',
                                                           'CP_X',
                                                           'CP_Y',
                                                           'CP_Z',
                                                           'OE_A',
                                                           'OE_B',
                                                           'OE_G',
                                                           'TLV_X',
                                                           'TLV_Y',
                                                           'TLV_Z',
                                                           'TAV_X',
                                                           'TAV_Y',
                                                           'TAV_Z'])
        df.to_csv(file_path , index = False)
        self.get_logger().info(f"Model states data saved to {file_path}")
    
    def save_meta_data(self):
        meta_df = pd.DataFrame(self.meta_data, columns = ['ID', 'csv_name', 'heightmap_name'])
        meta_folder_path = output_folder + '/' + self.dataset_type + '/individual_meta_data/'
        if not os.path.exists(meta_folder_path):
            os.makedirs(meta_folder_path)
        meta_file_path = os.path.join(meta_folder_path, f"{self.world_name}_{self.dataset_type}_meta_data.csv")
        meta_df.to_csv(meta_file_path, index = False)
        self.get_logger().info(f"Meta data saved to {meta_file_path}")
        
def main(args=None):
    rclpy.init(args=args)

    # Initialize PubsSubsManager
    pubsubs_manager = PubsSubsManager()
    
    world_name = pubsubs_manager.world_name
    dataset_type = pubsubs_manager.dataset_type
    n_sim = pubsubs_manager.i_sim
    # Wait for Gazebo and the robot model to be up
    while not get_model_state(pubsubs_manager, model_name, root_relative_entity_name):
        pubsubs_manager.get_logger().info(f"Waiting for {model_name} model to be up in Gazebo")
        rclpy.spin_once(pubsubs_manager, timeout_sec=1.0)
    pubsubs_manager.get_logger().info(f"{model_name} model loaded and found in Gazebo")
    
    for i_sim in range(pubsubs_manager.i_sim):
        trial_successful = False
        while not trial_successful:
            pubsubs_manager.get_logger().info(f" === Simulation {i_sim}/{n_sim} for map {world_name}")
            random_model_state = generate_random_model_state()
            set_model_state(pubsubs_manager, random_model_state)
            time.sleep(1)  # Allow the robot to settle down after spawning
            
            # Check if the vehicle is overturned
            current_state = get_model_state(pubsubs_manager, model_name, root_relative_entity_name)
            if current_state and is_overturned(current_state.pose.orientation):
                pubsubs_manager.get_logger().info(f"Vehicle is overturned, restarting trial {i_sim}")
                continue
            
            pubsubs_manager.start_new_simulation_try(world_name, dataset_type, i_sim, random_model_state.pose)
            start_t = pubsubs_manager.get_clock().now()
            
            twist_publisher_thread = threading.Thread(target=pubsubs_manager.publish_fixed_twist)
            twist_publisher_thread.start()
            
            while pubsubs_manager.get_clock().now() - start_t < sim_duration:
                rclpy.spin_once(pubsubs_manager, timeout_sec=0.1)
            
            pubsubs_manager.stop_vehicle()
            pubsubs_manager.get_logger().info(f"Simulation {i_sim} over")
            
            if len(pubsubs_manager.model_states_data) < 500:
                pubsubs_manager.get_logger().info(f"Insufficient data collected, restarting trial {i_sim}")
                continue
            
            folder_path = os.path.join(output_folder, dataset_type, world_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            csv_file_path = os.path.join(folder_path, f"{world_name}_{dataset_type}_{i_sim}.csv")
            pubsubs_manager.save_model_states_data_to_csv(csv_file_path)
            pubsubs_manager.model_states_data = []
            
            heightmap_name = f"{world_name}.png"
            prefix = dataset_type + '/' + world_name + '/'
            pubsubs_manager.meta_data.append([i_sim, prefix + os.path.basename(csv_file_path), heightmap_name])
            trial_successful = True
    
    pubsubs_manager.save_meta_data()    
    pubsubs_manager.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()