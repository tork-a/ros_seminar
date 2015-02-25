#!/usr/bin/env python
from moveit_commander import MoveGroupCommander
from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler
import rospy

if __name__ == '__main__':

    group = MoveGroupCommander("whole_arm")
    rospy.init_node("temp_arm_demo")
      	 
    #target_position = [0.12, 0.12, 0.02]
    target_position = [0.05, 0.0, 0.24] #home position
    target_orientation = Quaternion(*quaternion_from_euler(0.0, 1.571, 0.0, 'sxyz'))
    target_pose = Pose(Point(*target_position), target_orientation)
    group.set_pose_target(target_pose)
        
    group.go()

