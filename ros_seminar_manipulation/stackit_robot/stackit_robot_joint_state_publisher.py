#!/usr/bin/env python

"""
    stackit_robot_joint_state_publisher.py - Version 1.0 2010-12-28
    
    Publish the dynamixel_controller joint states on the /joint_states topic
    
    Created for the Pi Robot Project: http://www.pirobot.org
    Copyright (c) 2010 Patrick Goebel.  All rights reserved.

    Created for TORK: http://opensource-robotics.tokyo.jp/
    Copyright (c) 2014 Wataru Yasuda.  All rights reserved.

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details at:
    
    http://www.gnu.org/licenses/gpl.html
"""

import rospy
from sensor_msgs.msg import JointState as JointStateSensor
from dynamixel_msgs.msg import JointState as JointStateDynamixel
from collections import namedtuple
 
 
class Main():
    def __init__(self):
        rospy.init_node('stackit_robot_joint_state_publisher', anonymous=True)
        
        rate = rospy.get_param('~rate', 40)
        r = rospy.Rate(rate)
        
        # Start controller state subscribers
        self.JointStateMessage = namedtuple('JointStateMessage', 'name position velocity effort')
        self.joint_states = dict({})
        controllers = ['/base_lift_controller','/base_pan_controller','/elbow_flex_controller','/wrist_flex_controller']
        for controller in controllers:
            joint = rospy.get_param( controller + '/joint_name', '')
            
            self.joint_states[joint] = self.JointStateMessage(controller, 0.0, 0.0, 0.0)
            rospy.Subscriber( controller + '/state', JointStateDynamixel, self.controller_state_handler)
        
        # Start publisher
        self.joint_states_pub = rospy.Publisher('/joint_states', JointStateSensor)
        rospy.loginfo("Starting Joint State Publisher for Dynamixel at " + str(rate) + "Hz")
       
        while not rospy.is_shutdown():
            self.publish_joint_states()
            r.sleep()
           
    def controller_state_handler(self, msg):
        self.joint_states[msg.name] = self.JointStateMessage(msg.name, msg.current_pos, msg.velocity, msg.load)
               
    def publish_joint_states(self):
        # Construct message & publish joint states
        msg = JointStateSensor()
               
        for joint in self.joint_states.values():
            msg.name.append(joint.name)
            msg.position.append(joint.position)
            msg.velocity.append(joint.velocity)
            msg.effort.append(joint.effort)
           
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = 'base_link'
        self.joint_states_pub.publish(msg)
        
if __name__ == '__main__':
    try:
        Main()
    except rospy.ROSInterruptException: pass

