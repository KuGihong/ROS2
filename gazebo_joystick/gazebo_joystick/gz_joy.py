import rclpy	#import rclpy module

from rclpy.node import Node	#import Node from rclpy.node
from rclpy.qos import QoSProfile	#import QosProfile from rclpy.qos

from sensor_msgs.msg import Joy	#import QosPrfile from rclpy.qos
from geometry_msgs.msg import Twist	#import String from std_msgs.msg

class Teleop(Node):
	
     def __init__(self):
         super().__init__('gz_joy')
         qos_profile = QoSProfile(depth=10) #specify space to store data
         self.publisher_ = self.create_publisher(Twist,'/xycar/cmd_vel', qos_profile)
         #publish the topic in the form of the Twist message with 10 pieces of data
         self.subscriber_ = self.create_subscription(Joy,'/joy', self.Joy_callback,
         qos_profile)	
         #subscribe the topic in the form of the Joy message with 10 pieces of data
 	
     def Joy_callback(self, data):
         msg = Twist()
         msg.linear.x = 2*data.axes[1]	#vertical left stick axis = linear rate
         msg.angular.z = 2*data.axes[3]	#horizontal left stick axis = turn rate

         self.publisher_.publish(msg)
         self.get_logger().info('Linear: "%f"' % msg.linear.x) #showing log of information
         self.get_logger().info('Angular: "%f"' % msg.angular.z) #showing log of information


def main(args=None):
     rclpy.init(args=args)	#rclpy module initialized args
     
     joystick = Teleop()
     try:
        rclpy.spin(joystick)	#execute callback
     except KeyboardInterrupt:
        joystick.get_logger().info('Keyboard Interrupt (SIGHT)')
     finally:   
        joystick.destroy_node()	#destroy node
        rclpy.shutdown()	#exit


if __name__ == '__main__':
	main()
