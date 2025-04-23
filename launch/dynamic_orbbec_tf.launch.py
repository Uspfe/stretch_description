from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='stretch_description',  # Replace with your actual package name
            executable='dynamic_tf_broadcaster',  # Match the script filename (without .py)
            name='dynamic_tf_broadcaster',
            output='screen'
        )
    ])