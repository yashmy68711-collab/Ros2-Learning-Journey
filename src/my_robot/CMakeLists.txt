cmake_minimum_required(VERSION 3.8)

project(my_robot)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# -------------------------
# C++ Publisher
# -------------------------

add_executable(cpp_minimal_publisher
  src/cpp_minimal_publisher.cpp
)

ament_target_dependencies(cpp_minimal_publisher
  rclcpp
  std_msgs
)

# -------------------------
# C++ Subscriber
# -------------------------

add_executable(cpp_minimal_subscriber
  src/cpp_minimal_subscriber.cpp
)

ament_target_dependencies(cpp_minimal_subscriber
  rclcpp
  std_msgs
)

# -------------------------
# Install C++ executables
# -------------------------

install(
  TARGETS
    cpp_minimal_publisher
    cpp_minimal_subscriber
  DESTINATION lib/${PROJECT_NAME}
)

# -------------------------
# Install Python package
# -------------------------

ament_python_install_package(ros2_fundamentals_examples)

# -------------------------
# Testing
# -------------------------

if(BUILD_TESTING)

  find_package(ament_cmake_pytest REQUIRED)

  ament_add_pytest_test(
    minimal_publisher_test
    test/pytest/test_publisher.py
    TIMEOUT 60
  )

endif()

ament_package()