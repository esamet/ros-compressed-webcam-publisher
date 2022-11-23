import os
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([  
        Node(
            package='cv_basics',
            namespace='cv_basics',
            executable='webcam_pub',
            name='webcam_pub',
        )
])