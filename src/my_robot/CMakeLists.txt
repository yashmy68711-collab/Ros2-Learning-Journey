cmake_minimum_required(VERSION 3.8)
project(my_robot)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# C++ publisher
add_executable(cpp_minimal_publisher
  src/cpp_minimal_publisher.cpp
)

ament_target_dependencies(cpp_minimal_publisher
  rclcpp
  std_msgs
)

# Install C++ executable
install(
  TARGETS cpp_minimal_publisher
  DESTINATION lib/${PROJECT_NAME}
)

# Install Python nodes

install(
  PROGRAMS
    "${CMAKE_CURRENT_SOURCE_DIR}/ROS2 fundamental example/py_minimal_publisher.py"
    "${CMAKE_CURRENT_SOURCE_DIR}/ros2_fundamentals_examples/py_minimal_subscriber.py"
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()