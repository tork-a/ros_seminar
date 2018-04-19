#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
voice_cmd_vel.py is a simple demo of speech recognition.  You can
control a mobile robot using Android app named "ROS Voice Message".

ROS Voice Message:
https://play.google.com/store/apps/details?id=org.ros.android.android_voice_message
"""

import rospy
import math
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from jsk_gui_msgs.msg import VoiceMessage

class voice_cmd_vel:

    def __init__(self):
        rospy.on_shutdown(self.cleanup)
        self.linear_speed = 0.2
        self.angular_speed = 0.2
        self.msg = Twist()

        # publish to cmd_vel, subscribe to speech output
        self.pub_ = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/Tablet/voice', VoiceMessage, self.speechCb)

        r = rospy.Rate(10.0)
        while not rospy.is_shutdown():
            self.pub_.publish(self.msg)
            r.sleep()
        
    def speechCb(self, msg):
        text = msg.texts[0]
        rospy.loginfo(text)
        self.linear_speed = 0.2
        if text.find("速") > -1 or text.find("早") > -1:
            self.linear_speed = 0.3
        elif text.find("遅") > -1 or text.find("ゆっくり"):
            self.linear_speed = 0.1
        if text.find("前") > -1:    
            self.msg.linear.x = self.linear_speed
        elif text.find("後") > -1:
            self.msg.linear.x = -self.linear_speed
        if text.find("左") > -1:
            self.msg.angular.z = self.angular_speed
        elif text.find("右") > -1:    
            self.msg.angular.z = -self.angular_speed
        elif text.find("まっすぐ") > -1 or text.find("直") > -1:
            self.msg.angular.z = 0
        if text.find("止") > -1 or text.find("ストップ") > -1:          
            self.msg = Twist()
        
        self.pub_.publish(self.msg)

    def cleanup(self):
        # stop the robot!
        twist = Twist()
        self.pub_.publish(twist)

if __name__=="__main__":
    rospy.init_node('voice_cmd_vel')
    try:
        voice_cmd_vel()
    except:
        pass

