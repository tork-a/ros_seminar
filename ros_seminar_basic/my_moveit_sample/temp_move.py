#!/usr/bin/env python
from moveit_commander import MoveGroupCommander
import rospy

if __name__ == '__main__':
    group = MoveGroupCommander("manipulator")
    rospy.init_node("vs060_demo_wy")
    temp_pose=group.get_current_pose()
    temp_pose.pose.position.z = temp_pose.pose.position.z - 0.1
    group.set_pose_target(temp_pose)
    group.go()
