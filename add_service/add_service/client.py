import sys  # Import sys module to receive arguments from terminal commands

from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node

class Client(Node):
     def __init__(self):

         super().__init__('client') # Node name is 'client'
         self.cli = self.create_client(AddTwoInts, 'service')   # Create service
         while not self.cli.wait_for_service(timeout_sec=1.0): # The client's wait_for_service function checks if the service exists.
             self.get_logger().info('service not available, waiting again...')
             self.req = AddTwoInts.Request()    # Set the request message to the req property
             
     def send_request(self):
         # Variables entered in the terminal through the sys module are passed to a and b of the request message.
         self.req.a = int(sys.argv[1])
         self.req.b = int(sys.argv[2])
         
         # Send a request message to the server via the client's call_async function and wait for a response.
         self.future = self.cli.call_async(self.req)
     
def main(args=None):

     rclpy.init(args=args)
     
     # Send a request message to the server and receive a response message
     client = Client() 
     client.send_request()

     while rclpy.ok():
         rclpy.spin_once(client) # Run only once through the spin_once function.
         if client.future.done():
             try:
                 response = client.future.result()
             except Exception as e:
                 client.get_logger().info('Service call failed % r' % (e, )) # Display failed information on the screen
             else:
                 # Display reponsed information on the screen
                 client.get_logger().info('Result of add_two_ints: for %d + %d = %d' % (client.req.a, client.req.b, response.sum))
             break
         
     client.destroy_node() # destroy node
     rclpy.shutdown() # exit
     
if __name__ == '__main__':
    main()
