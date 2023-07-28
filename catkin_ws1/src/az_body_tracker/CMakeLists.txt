cmake_minimum_required(VERSION 3.5)
project(az_body_tracker)
# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()
list(INSERT CMAKE_MODULE_PATH 0 ${CMAKE_CURRENT_LIST_DIR}/cmake)
set(glfw3_DIR "/usr/local/lib/cmake/glfw3")

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()
add_subdirectory(window_controller_3d)
# find dependencies
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  sensor_msgs
  genmsg
  
  message_generation
)

generate_messages(DEPENDENCIES std_msgs sensor_msgs)
find_package(k4a 1.4.1 QUIET MODULE REQUIRED)
find_package(k4abt 1.1.2 QUIET MODULE REQUIRED)

include_directories(${catkin_INCLUDE_DIRS} include src)

add_executable(az_body_tracker src/az_body_tracker.cpp src/TrackerNode.cpp include/TrackerNode.h)
target_link_libraries(az_body_tracker 
k4abt::k4abt 
k4a::k4a 
window_controller_3d::window_controller_3d
${catkin_LIBRARIES}
)
target_include_directories(az_body_tracker PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
add_dependencies(az_body_tracker az_body_tracker_generate_messages_cpp)

install(TARGETS az_body_tracker
  DESTINATION lib/${PROJECT_NAME})
catkin_package(CATKIN_DEPENDS message_runtime std_msgs sensor_msgs)

