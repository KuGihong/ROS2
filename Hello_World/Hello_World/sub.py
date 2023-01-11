import rclpy	#import rclpy module
from rclpy.node import Node	#import Node from rclpy.node
from rclpy.qos import QoSProfile	#import QosPrfile from rclpy.qos

from std_msgs.msg import String	#import String from std_msgs.msg

class Sub(Node): 	#declare class Pub
	
     def __init__(self):
         super().__init__('sub')	#Node calss's name is sub
         qos_profile = QoSProfile(depth=10)
         self.subscriber_ = self.create_subscription(String,'topic', self.listener_callback,
         qos_profile) #subscriber subscription messages of type String to the topic
 	
 	
     def listener_callback(self, msg):
         self.get_logger().info('I heard: "%s"' % msg.data) #showing log of information

	
def main(args=None):

     rclpy.init(args=args)	#rclpy module initialized args
     node = Sub()
     try:
         rclpy.spin(node)	#execute node(pub)
     except KeyboardInterrupt:
         node.get_logger().info('Keyboard Interrupt (SIGINT)')
     finally:
         node.destroy_node()	#destroy node
         rclpy.shutdown()	#exit
         
if __name__ == '__main__':
	main()
