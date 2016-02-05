#!/usr/bin/env python

import rospy
import geometry_msgs.msg

from moveit_commander import MoveGroupCommander

if __name__ == '__main__':
    rospy.init_node('commander_example', anonymous=True)
    group = MoveGroupCommander("right_arm")
    group.set_planner_id('RRTConnectkConfigDefault')

    pose_rarm_curr = group.get_current_pose('RARM_JOINT5_Link')
    rospy.loginfo('Current pose: {}'.format(pose_rarm_curr))

    # right hand move to approx. 2cm ahead
    pose_target = geometry_msgs.msg.Pose()
    pose_target.position.x = 0.392
    pose_target.position.y = -0.182
    pose_target.position.z = 0.0748
    pose_target.orientation.y = -0.708
    pose_target.orientation.w = 0.706
    rospy.loginfo("set target to {}".format(pose_target))
    group.set_pose_target(pose_target)
    plan = group.plan()
    rospy.loginfo("plan is {}".format(plan))
    ret = group.go()
    rospy.loginfo("Command ran ... {}".format(ret))

    pose_rarm_curr = group.get_current_pose('RARM_JOINT5_Link')
    rospy.loginfo('Pose after: {}'.format(pose_rarm_curr))
