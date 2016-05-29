^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package stackit_robot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.0.2 (2016-05-29)
------------------
* update all packge version to 1.0.1
* stackit_robot_joint_state_publisher.py: joint_states need joint name, not controller name
* use joint_trajectory_action_controller with https://github.com/arebgun/dynamixel_motor/issues/33
* stackit_robot/dynamixel_all.launch: forget to pass arguments
* [stackit] Minor formatting
* [stackit] Separate launch files for when slower machines cannot handle controllers well.
* [stackit] Fix duplicate rviz run upon dynamixel_moveit.launch
* [stackit_robot/dynamixel_all.launch] Stop kicking start_controllers.launch that may not work if called within this launch file
* Contributors: Isaac I.Y. Saito, Moirai, Tokyo Opensource Robotics Programmer 534o

1.0.1 (2015-05-14)
------------------
* Revert "Add USB port arg." -- We were not able to confirm that these commits function as intended (when typing in `port_name` in `ontroller_manager.launch`, the value seems to have been read fine.
  This reverts commit 19e70b66f4e5712cf884a2b43f9c781c463260fd.
* RViz with gdb option
* Add USB port arg.
* More workaround for RViz core dump.
* Workaround for RViz core dump.
* [Intermediate] Minor improvement
* Filename typo
* Fix lang setting error.
* Add marker_demo
* Add move_arm files.
* Add license, author and maintainers.
* Add all-in-1 launch files.
* Wrong format.
* (ROS seminar pkg) Init commit.
* Contributors: Isaac IY Saito
