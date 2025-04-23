""" Static transform publisher acquired via MoveIt 2 hand-eye calibration """
""" EYE-IN-HAND: link_head_tilt -> camera_color_optical_frame """
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    nodes = [
        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            output="log",
            arguments=[
                "--frame-id",
                "link_head_tilt",
                "--child-frame-id",
                "camera_color_optical_frame",
                "--x",
                "0.031591",
                "--y",
                "-0.0119208",
                "--z",
                "0.0807607",
                "--qx",
                "-0.489168",
                "--qy",
                "0.51206",
                "--qz",
                "-0.507018",
                "--qw",
                "0.491368",
                # "--roll",
                # "1.64804",
                # "--pitch",
                # "1.53215",
                # "--yaw",
                # "3.0716",
            ],
        ),
    ]
    return LaunchDescription(nodes)
