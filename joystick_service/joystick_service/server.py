import rclpy

from sensor_msgs.msg import Joy
from rclpy.node import Node
#from std_srvs.srv import Empty
from turtlesim.srv import Spawn

class Server(Node):
    def __init__(self):
        super().__init__('server')
        self.srv_server = self.create_service(Spawn, '/spawn', self.callback)
        self.req = Spawn.Response()
        
    def callback(self, req, res):
         res.name = str(req.x) + str(req.y) + str(req.theta) + req.name
         self.get_logger().info('Incoming request\n x: %f y: %f theta: %f name: %s res.name: %s' % (req.x, req.y, req.theta, req.name, res.name))
         return res

    
def main(args=None):

     rclpy.init(args=args)  

     server = Server()

     rclpy.spin(server) 

     rclpy.shutdown() 
     
if __name__ == '__main__':
    main()
