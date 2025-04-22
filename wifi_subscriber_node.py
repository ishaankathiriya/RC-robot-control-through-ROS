import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import socket
import json

class WifiSubscriberNode(Node):
    def __init__(self):
        super().__init__('wifi_subscriber_node')
        self.esp_ip = '192.168.4.1'
        self.esp_port = 81
        self.connected = None
        self.connect_to_esp()
        self.wifi_sub = self.create_subscription(Twist,'/turtle1/cmd_vel', self.callback_command, 10)
        self.current_left_pwm = 0
        self.current_right_pwm = 0
        


    def give_pwm(self, num):
        return max(-255,min(255, num))

    def callback_command(self, msg:Twist):
        
        linear = msg.linear.x
        angular = msg.angular.z
        
        # now these values need to be converted to left PWM and Right PWM
        # PWM range: -255 to 255

        
        self.current_left_pwm = self.give_pwm(linear - angular)
        self.current_right_pwm = self.give_pwm(linear + angular)

        lst = [self.current_left_pwm, self.current_right_pwm]



        data = json.dumps(lst)
        self.sock.send(data.encode())
        self.get_logger().info(f'Sent: {json.loads(data)}')



    def connect_to_esp(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.esp_ip,self.esp_port))
        # self.sock.send(b'hmmmmm')
        self.connected = True
        self.get_logger().info('Connected to ESP via WiFi')


def main(args = None):
    rclpy.init(args=args)
    node = WifiSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

