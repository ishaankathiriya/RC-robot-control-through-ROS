#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import socket
import time

class WifiPublisherNode(Node):
    def __init__(self):
        super().__init__('wifi_node')

        self.esp_ip = '192.168.4.1'
        self.esp_port = 81
        self.connected = None
        self.connect_to_esp()
        #self.timer = self.create_timer(10, self.check_connection())
        self.wifi_subscriber = self.create_subscription(String, 'commands', self.callback_commands,10)
 

    def callback_commands(self, msg:String):
        self.sock.send(msg.data.encode())
        self.get_logger().info(f'Sent: {msg.data}')

    # def check_connection(self):
    #     if not self.connected:
    #         self.get_logger().info('Trying to reconnect to ESP32 AP...')
    #         self.connect_to_esp()


    def connect_to_esp(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.esp_ip,self.esp_port))
        self.sock.send(b'hmmmmm')
        self.connected = True
        self.get_logger().info('Connected to ESP via WiFi')



def main(args = None):
    rclpy.init(args = args)
    node = WifiPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
