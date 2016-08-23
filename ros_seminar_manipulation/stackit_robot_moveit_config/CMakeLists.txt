cmake_minimum_required(VERSION 2.8.3)
project(stackit_robot_moveit_config)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(DIRECTORY config DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

## test
if(CATKIN_ENABLE_TESTING)
  find_package(catkin REQUIRED COMPONENTS rostest roslaunch)
  file(GLOB LAUNCH_FILES launch/demo.launch launch/move_group.launch launch/moveit_rviz.launch test/*.test)
  foreach(LAUNCH_FILE ${LAUNCH_FILES})
    roslaunch_add_file_check(${LAUNCH_FILE})
  endforeach()
endif()
