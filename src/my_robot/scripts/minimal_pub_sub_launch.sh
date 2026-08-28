#!/bin/bash

# Cleanup function
cleanup() {
    echo "Stopping ROS 2 nodes..."
    kill 0
    exit
}

# Run cleanup when Ctrl+C is pressed
trap cleanup SIGINT

# Start publisher
ros2 run my_robot py_minimal_publisher.py &

# Wait 2 seconds
sleep 2

# Start subscriber
ros2 run my_robot py_minimal_subscriber.py