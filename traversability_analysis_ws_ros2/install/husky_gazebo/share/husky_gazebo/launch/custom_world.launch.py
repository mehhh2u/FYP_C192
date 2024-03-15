from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


# ros2 launch husky_gazebo custom_world.launch.py world_name:='world_name.world'

def generate_launch_description():
    
    # Declare a launch argument for the world file name
    declare_world_arg = DeclareLaunchArgument(
        'world_name', 
        default_value='clearpath_playpen.world',  # Default world file
        description='Name of the Gazebo world file')

    # Set the world file path using the launch argument
    world_file = PathJoinSubstitution(
        [FindPackageShare("husky_gazebo"),  # husky_gazebo package
         "worlds",                          # worlds subfolder
         LaunchConfiguration('world_name')], # world file name from the argument
    )

    gazebo_launch = PathJoinSubstitution(
        [FindPackageShare("husky_gazebo"),
         "launch",
         "gazebo.launch.py"],
    )

    gazebo_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([gazebo_launch]),
        launch_arguments={'world_path': world_file}.items(),
    )

    ld = LaunchDescription()
    ld.add_action(declare_world_arg)
    ld.add_action(gazebo_sim)

    return ld
