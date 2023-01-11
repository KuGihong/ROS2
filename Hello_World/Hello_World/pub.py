import rclpy	#import rclpy module
from rclpy.node import Node	#import Node from rclpy.node
from rclpy.qos import QoSProfile	#import QosPrfile from rclpy.qos

from std_msgs.msg import String	#import String from std_msgs.msg

class Pub(Node): 	#declare class Pub
	
     def __init__(self):
         super().__init__('pub')	#Node calss's name is pub
         qos_profile = QoSProfile(depth=10)
         self.publisher_ = self.create_publisher(String,'topic', qos_profile) 
         #publisher publishes messages of type String to the topic
 	
         timer_period = 0.5 #0.5 seconds timer
         self.timer = self.create_timer(timer_period, self.timer_callback)
         #timer calls back every 0.5 seconds
 	
         self.count = 0	#count initialized 0
 	
     def timer_callback(self):
         msg = String()
         msg.data = 'Hello World: %d' % self.count #published message
         self.publisher_.publish(msg)
         self.get_logger().info('Publishing: "%s"' % msg.data) #showing log of information
         self.count += 1 #when the function is called, increments by 1
	
def main(args=None):

     rclpy.init(args=args)	#rclpy module initialized args
     node = Pub()
     try:
         rclpy.spin(node)	#execute node(pub)
     except KeyboardInterrupt:
         node.get_logger().info('Keyboard Interrupt (SIGINT)')
     finally:
         node.destroy_node()	#destroy node
         rclpy.shutdown()	#exit
         
if __name__ == '__main__':
	main()
