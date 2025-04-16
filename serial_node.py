#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial


class SerialNode (Node):
    def __init__(self):
        super().__init__('serial_node')
        self.serial_subscriber_ = self.create_subscription(String, 'commands', self.callback_commands, 10)
        self.serial_ = serial.Serial('/dev/ttyACM0', 115200)
        self.get_logger().info('Serial started')


    def callback_commands (self, msg:String):
        self.get_logger().info(f'Sending command : {msg.data}')
        self.serial_.write(msg.data.encode())

    
def main(args = None):
    rclpy.init(args = args)
    node = SerialNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()




