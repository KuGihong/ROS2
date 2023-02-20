import rclpy

#from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from rclpy.node import Node
#from std_srvs.srv import Empty
from turtlesim.srv import Spawn

class Client(Node):
    def __init__(self):
        super().__init__('client')
        self.sub_joy = self.create_subscription(Joy, '/joy', self.joy_callback, 10)        
        self.srv_client = self.create_client(Spawn, '/spawn')
        while not self.srv_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again. . .')       
        self.req = Spawn.Request()
        self.type = 0
        
    def joy_callback(self, data):
        if data.buttons[0] == 1:
            self.get_logger().info('Service call: Spawn')    
            self.type = 1                      
        elif data.buttons[1] == 1:
            self.get_logger().info('Service call: Kill')    
            self.type = 2
        elif data.buttons[2] == 1:
            self.get_logger().info('Service call: Clear')    
            self.type = 3
        elif data.buttons[3] == 1:
            self.get_logger().info('Service call: Reset')    
            self.type = 4                    
        else:
            self.get_logger().info('No button') 
                                     
    def send_request(self):
            self.get_logger().info('type is %d' % self.type)     
            self.req.x = float(3.0)
            self.req.y = float(3.0)
            self.req.theta = float(0.0)
            self.req.name = "turtle1"
            self.future = self.srv_client.call_async(self.req)
            
def main(args=None):
    rclpy.init(args=args)
    
    client = Client()
    client.send_request()
    
    rclpy.spin(client)
    if client.future.done():
         try:
            response = client.future.result()
         except Exception as e:
            client.get_logger().info('Clear Service call failed %r' % (e, ))
         else:
            client.get_logger().info('Success\n x: %f y: %f theta: %f name: %s' % (client.req.x, client.req.y, client.req.theta, 
                                                                                   client.req.name, response.res.name))
        
        
    client.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()