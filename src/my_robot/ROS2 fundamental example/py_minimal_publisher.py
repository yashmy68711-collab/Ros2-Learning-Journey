#!/usr/bin/env python3

"""
Description:
    This ROS 2 node periodically publishes
    "Hello World" message to a topic.

------

Publishing Topics:
    The channel containing the "hello world" message
    /py_example_topic std_msgs / String

Subscription Topics:
    None

------

Author: Addison Sears-Collins
Date: Aug 27, 2026
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPyPublisher(Node):

    def __init__(self):
        """
        Create a minimal publisher node.
        """

        super().__init__('minimal_py_publisher')

        # Create a publisher
        self.publisher_1 = self.create_publisher(String,'/py_example_topic',10)

        # Create a timer with a period of 0.5 seconds

        timer_period = 0.5
        self.timer = self.create_timer(timer_period,self.timer_callback)

        # Initialize counter
        self.i = 0

    def timer_callback(self):
        """
        Callback function executed periodically by the timer.
        """

        # Create a String message
        msg = String()

        # Set message data
        msg.data = 'Hello World: %d' % self.i

        # Publish the message
        self.publisher_1.publish(msg)

        # Display the message in the terminal
        self.get_logger().info('Publishing: "%s"' % msg.data)

        # Increase counter
        self.i += 1

def main(args=None):
    """
    Main function to start the ROS 2 node.
    """

    # Initialize ROS 2
    rclpy.init(args=args)

    # Create publisher node
    minimal_py_publisher = MinimalPyPublisher()

    # Keep the node running
    rclpy.spin(minimal_py_publisher)

    # Destroy the node
    minimal_py_publisher.destroy_node()

    # Shutdown ROS 2
    rclpy.shutdown()


if __name__ == '__main__':
    main()