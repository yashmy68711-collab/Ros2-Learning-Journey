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

