#!/usr/bin/env python3


import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import pygame
import time



msg = 'Press W to move forward. S to go reverse. D to turn right, A for left. Q to quit'
class KeyboardTeleopNode(Node):
    def __init__(self):
        super().__init__('keyboard_teleop')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.linear_x = 0.0
        self.current_angular_vel = 0.0
        self.max_speed = 255
        self.min_speed = -255
        self.acceleration = 10
        self.angular_vel = 44
        self.twist = Twist()

        self.active_keys = set()


        # self.settings = termios.tcgetattr(sys.stdin)

        self.get_logger().info(msg)



        pygame.init()
        # Required even if you don't need graphics
        screen = pygame.display.set_mode((300, 300))  
        pygame.display.set_caption("Key Press Test")
        #rclpy.spin_once(self, timeout_sec=0.1)
        # while not self.active_keys:
        #     print('asdfdgdfg')
        #     self.current_angular_vel =0.0
        #     while self.linear_x != 0: 
        #         if self.linear_x > 0:
        #             self.linear_x -= self.acceleration
        #         elif self.linear_x < 0:
        #             self.linear_x += self.acceleration
        #     self.twist.linear.x = self.linear_x
        #     self.twist.angular.z = self.current_angular_vel
        #     self.publisher.publish(self.twist)

        # rclpy.spin_once(self, timeout_sec=0.1)




    def w_pressed(self):
        if self.linear_x < self.max_speed:
            self.linear_x += self.acceleration
                
        elif self.linear_x > self.max_speed:
            self.linear_x = self.max_speed



    def s_pressed(self):
        if self.linear_x > self.min_speed:
            self.linear_x -= self.acceleration
                
        elif self.linear_x < self.min_speed:
            self.linear_x = self.min_speed

    def a_pressed(self):
        
            self.current_angular_vel = self.angular_vel
        

    def d_pressed(self):
        
            self.current_angular_vel = -self.angular_vel

    def nothing_pressed(self):
        
        if self.linear_x > 0:
            self.linear_x -= self.acceleration
            if self.linear_x < 0:
                self.linear_x = 0.0

        elif self.linear_x < 0:
            self.linear_x += self.acceleration
            if self.linear_x > 0:
                self.linear_x = 0.0

        self.current_angular_vel = 0.0
    

    # def keys_pressed(self):
        
    #     if keyboard.is_pressed('w'):
    #         self.active_keys.add('w')

    #     if keyboard.is_pressed('a'):
    #         self.active_keys.add('a')

    #     if keyboard.is_pressed('s'):
    #         self.active_keys.add('s')

    #     if keyboard.is_pressed('d'):
    #         self.active_keys.add('d')

    #     if keyboard.is_pressed('w') and keyboard.is_pressed('d'):
    #         self.active_keys.add('w','d')

    #     if keyboard.is_pressed('w') and keyboard.is_pressed('a'):
    #         self.active_keys.add('w','d')
        
    #     if keyboard.is_pressed('w') and keyboard.is_pressed('d'):
    #         self.active_keys.add('w','d')

    #     if keyboard.is_pressed('w') and keyboard.is_pressed('d'):
    #         self.active_keys.add('w','d')

    #     if keyboard.is_pressed('w') and keyboard.is_pressed('d'):
    #         self.active_keys.add('w','d')

        

    def timer_callback(self):
        pygame.event.pump()
        self.active_keys =  set()
        

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.active_keys.add('w')

        if keys[pygame.K_s]:
            self.active_keys.add('s')

        if keys[pygame.K_a]:
            self.active_keys.add('a')

        if keys[pygame.K_d]:
            self.active_keys.add('d')

        if keys[pygame.K_q]:
            self.get_logger().info('Quitting')
            exit()


        if 'w' in self.active_keys:
            self.w_pressed()
            print("w pressed")

        if 's' in self.active_keys:
            self.s_pressed()

        # if 'w' not in self.active_keys and 's' not in self.active_keys:
        #      self.nothing_pressed()

        if 'a' in self.active_keys:
            self.a_pressed()

        if 'd' in self.active_keys:
            self.d_pressed()

        if 'w' not in self.active_keys and 's' not in self.active_keys and 'a' not in self.active_keys and 'd' not in self.active_keys:     
            self.nothing_pressed()
             
             
        # if 'w' in self.active_keys:
        #     while self.linear_x != self.max_speed:
        #         self.linear_x += self.acceleration

        # if 's' in self.active_keys:
        #     while self.linear_x != self.min_speed:
        #         self.linear_x -= self.acceleration

        # if 'w' not in self.active_keys and 's' not in self.active_keys:
        #     if self.linear_x > 0:
        #         while self.linear_x != 0:
        #             self.linear_x -= self.acceleration

        #     if self.linear_x < 0:
        #         while self.linear_x != 0:
        #             self.linear_x += self.acceleration

        # self.current_angular_vel = 0

        # if 'a' in self.active_keys:
        #     self.current_angular_vel = self.angular_vel

        # if 'd' in self.active_keys:
        #     self.current_angular_vel = -self.angular_vel


        
        self.twist.linear.x = float(self.linear_x)
        self.twist.angular.z = float(self.current_angular_vel)
        self.publisher.publish(self.twist)


        self.get_logger().info(f'Published: speed: {self.twist.linear.x}\n angular speed : {self.twist.angular.z}, keys pressed : {self.active_keys}')
        pygame.event.pump() # process event queue




def main(args=None):
    rclpy.init(args = args)
    node = KeyboardTeleopNode()
    rclpy.spin(node)
    
    
        

    rclpy.shutdown()

if __name__ == '__main__':
    main()