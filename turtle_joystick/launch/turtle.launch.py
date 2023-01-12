from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import LogInfo

def generate_launch_description():	#function to run the Nodes
    return LaunchDescription([
        LogInfo(msg=['Running a turtlesim moving file with a joystick!']),
        #message printed to the console

        Node(	#turtlesim node
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim',
            output='screen'
        ),

        Node(	#turtle_joystick node
            package='turtle_joystick',
            executable='turtle_joy',
            name='turtle_joystick',
            output='screen'
        ),

        Node(	#joy node
            package='joy',
            executable='joy_node',
            name='joy',
        )
    ])
