#!/usr/bin/env python

import rospy

from std_msgs.msg import String
from geometry_msgs.msg import Twist

class Sender:
    def __init__(self):
        self.msg = Twist()
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        rospy.Subscriber('text', String, self.callback)
        rate = rospy.Rate(10.0)
        while not rospy.is_shutdown():
            self.pub.publish(self.msg)
            rate.sleep()

    def callback(self, msg):
        rospy.loginfo(msg.data)
        if 'forward' in msg.data:
            self.msg.linear.x = 0.2
            self.msg.angular.z = 0.0
        if 'back' in msg.data:
            self.msg.linear.x = -0.2
            self.msg.angular.z = 0.0
        if 'left' in msg.data:
            self.msg.linear.x = 0.0
            self.msg.angular.z = 0.1
        if 'right' in msg.data:
            self.msg.linear.x = 0.0
            self.msg.angular.z = -0.1
        if 'stop' in msg.data:
            self.msg.linear.x = 0.0
            self.msg.angular.z = 0.0

if __name__=="__main__":
    rospy.init_node('send_vel_with_text')
    Sender()
