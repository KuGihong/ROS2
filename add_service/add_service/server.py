from example_interfaces.srv import AddTwoInts   # Import AddTwoInts module

import rclpy    #Import rclpy and Node module
from rclpy.node import Node

class Server(Node):
     def __init__(self):

         super().__init__('server') # Node name is 'server'
         self.srv = self.create_service(AddTwoInts, 'service', self.callback) # Create service

     def callback(self, req, res):
         res.sum = req.a + req.b    # Response sum = request a + b
         self.get_logger().info('Incoming request\na: %d b: %d' % (req.a, req.b)) # Display requested information on the screen

         return res # Res return
     
def main(args=None):

     rclpy.init(args=args)  # rclpy module initialized args

     server = Server()

     rclpy.spin(server) # #execute callback

     rclpy.shutdown() # #exit
     
if __name__ == '__main__':
    main()


