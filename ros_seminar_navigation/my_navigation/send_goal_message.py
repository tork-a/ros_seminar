#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped

if __name__ == '__main__':
    rospy.init_node('send_goal_message', anonymous=True)
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)

    # wait for /clock for simulation
    rospy.sleep(1)

    msg = PoseStamped()
    msg.header.stamp = rospy.Time.now()
    msg.header.frame_id = "map"
    msg.pose.position.x=33;
    msg.pose.position.y=33;
    msg.pose.orientation.w = 1
    print msg
    pub.publish(msg)

