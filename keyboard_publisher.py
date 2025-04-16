#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import sys
import termios
import tty

class KeyboardPublisher(Node):
    def __init__(self):
        super().__init__('keyboard_publisher')
        self.keybboard_publisher_ = self.create_publisher(String, 'commands', 10)
        self.get_logger().info('Keyboard Publisher started. Press W, A, S, D to move.  Q to Quit. E to stop')
        self.run()

    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        tty.setraw(fd)
        key = sys.stdin.read(1)
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key
    
    def run(self):
        while rclpy.ok():
            key = self.get_key()
            msg = String()
            
            if key.lower() in ['w', 'a', 's', 'd', 'e']:
                msg.data = key.lower()
                self.keybboard_publisher_.publish(msg)
                self.get_logger().info(f'Published key : {msg.data}')

            elif key.lower() == 'q':
                self.get_logger().info('Exiting')
                break



def main(args = None):
    rclpy.init(args = args)
    node = KeyboardPublisher()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()

