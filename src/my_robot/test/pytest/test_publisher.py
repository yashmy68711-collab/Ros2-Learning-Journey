import pytest
import rclpy

from std_msgs.msg import String

from ros2_fundamentals_examples.py_minimal_publisher import MinimalPyPublisher


def test_node_creation():
    """
    Test that the MinimalPyPublisher node can be created successfully.
    """
    rclpy.init()

    try:
        node = MinimalPyPublisher()

        assert node is not None
        assert node.i == 0

    finally:
        rclpy.shutdown()


def test_initial_counter():
    """
    Test that the message counter starts at 0.
    """
    rclpy.init()

    try:
        node = MinimalPyPublisher()

        assert node.i == 0

    finally:
        rclpy.shutdown()


def test_message_counter():
    """
    Test if the message counter increments correctly.

    The timer callback should increase the counter by 1.
    """
    rclpy.init()

    try:
        node = MinimalPyPublisher()

        initial_count = node.i

        node.timer_callback()

        assert node.i == initial_count + 1

    finally:
        rclpy.shutdown()


def test_message_content():
    """
    Test if the message content is formatted correctly.

    When the counter is 5, the expected message is:
    'Hello World: 5'
    """
    rclpy.init()

    try:
        node = MinimalPyPublisher()

        node.i = 5

        msg = String()
        msg.data = f'Hello World: {node.i}'

        assert msg.data == 'Hello World: 5'

    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    pytest.main(['-v'])