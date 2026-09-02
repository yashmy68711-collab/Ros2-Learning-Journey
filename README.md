# ROS 2 Learning Journey

My journey learning ROS 2, robotics, simulation, robot control, and motion planning.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Day 1 — ROS 2 Basics & Package Setup

### What I learned

- Installed and configured ROS 2 Jazzy on Ubuntu.
- Learned the basic ROS 2 workspace structure.
- Created and worked with a ROS 2 workspace.
- Learned about the `src`, `build`, `install`, and `log` directories.
- Learned the basic structure of a ROS 2 package.
- Created my ROS 2 package.
- Learned about `package.xml`.
- Learned about `CMakeLists.txt`.
- Learned how ROS 2 packages are built using `colcon`.
- Learned how to source the ROS 2 workspace.
- Used VS Code with the ROS 2 workspace.
- Connected my ROS 2 learning project to GitHub.
- Learned the basic Git workflow for saving my ROS 2 work.

### Workspace Structure

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Day 2 — ROS 2 Python Publisher

### What I learned

- Created my first ROS 2 Python Publisher node.
- Learned how to use `rclpy` in a Python ROS 2 program.
- Learned how to create a ROS 2 Node using `Node`.
- Learned how to create a Publisher using `create_publisher()`.
- Learned about ROS 2 Topics.
- Used the `std_msgs/msg/String` message type.
- Created the topic `/py_example_topic`.
- Used a timer to publish messages periodically.
- Published `Hello World` messages with an increasing counter.
- Learned how `rclpy.spin()` keeps the node running.
- Learned how to initialize ROS 2 using `rclpy.init()`.
- Learned how to properly destroy a node using `destroy_node()`.
- Learned how to shut down ROS 2 using `rclpy.shutdown()`.
- Updated `CMakeLists.txt` so the Python publisher could be installed and executed.
- Built the package successfully using `colcon build`.
- Sourced the workspace and verified the executable.
- Successfully ran the publisher from the terminal.

### Publisher File

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## Day 3 — ROS 2 Python Subscriber & Publisher-Subscriber Communication

### What I learned

- Created my first ROS 2 Python Subscriber node.
- Learned how a Subscriber receives messages from a ROS 2 topic.
- Used `rclpy` and the ROS 2 `Node` class.
- Used `std_msgs/msg/String` for receiving messages.
- Learned how to create a subscription using `create_subscription()`.
- Learned how callback functions work in ROS 2.
- Connected the Subscriber to the `/py_example_topic` topic.
- Tested communication between the Publisher and Subscriber.
- Learned how a Publisher sends messages and a Subscriber receives them.
- Updated `CMakeLists.txt` to install the Subscriber executable.
- Used `ros2 pkg executables` to verify the available executables.
- Created a Bash script to start both Publisher and Subscriber.
- Learned how to run ROS 2 nodes from a Bash script.
- Used `&` to run the Publisher in the background.
- Used `sleep` to wait before starting the Subscriber.
- Learned how `trap` and `SIGINT` can be used for cleanup.
- Used `Ctrl+C` to stop the running ROS 2 processes.
- Used `chmod +x` to make the Bash script executable.
- Successfully built and tested the complete Publisher-Subscriber system.

### Result

Successfully ran the Publisher and Subscriber together and verified that messages were being published and received through the ROS 2 topic.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Day 4 — ROS 2 C++ Publisher

### What I learned

- Created my first ROS 2 C++ Publisher node.
- Learned how to create a ROS 2 C++ node using `rclcpp`.
- Learned how to use the `rclcpp::Node` class.
- Used `std_msgs/msg/String` for publishing string messages.
- Created a Publisher using `create_publisher()`.
- Created a timer using `create_wall_timer()`.
- Used a timer callback to publish messages periodically.
- Published messages on the `/cpp_example_topic` topic.
- Used a counter to create continuously increasing messages.
- Learned how `publisher_->publish()` sends messages to a ROS 2 topic.
- Learned how to initialize and shut down ROS 2 in C++.
- Updated `CMakeLists.txt` to build and install the C++ executable.
- Updated `package.xml` with the required C++ dependencies.
- Built the ROS 2 package successfully using `colcon build`.
- Ran the C++ publisher successfully using `ros2 run`.
- Verified the topic using `ros2 topic list`.
- Verified the published messages using `ros2 topic echo`.
- Confirmed that the publisher was publishing messages at 2 Hz.

- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Day 5 — C++ Publisher in ROS 2

Today I learned how to create a basic **C++ Publisher Node** in ROS 2.

### What I Learned

- How to create a C++ ROS 2 node using `rclcpp`
- How to create a publisher using `create_publisher()`
- How to publish messages using `std_msgs/msg/String`
- How to use a timer to publish messages at a fixed rate
- How to add a C++ executable in `CMakeLists.txt`
- How to build the package using `colcon build`
- How to run a C++ node using `ros2 run`
- How to inspect a topic using ROS 2 CLI commands

### C++ Publisher

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
