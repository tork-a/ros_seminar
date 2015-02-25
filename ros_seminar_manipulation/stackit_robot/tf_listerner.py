#!/usr/bin/env python  
import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('tf_listener')
    listener = tf.TransformListener()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans1,rot) = listener.lookupTransform('/base_link', '/marker_1_target', rospy.Time(0))
            (trans2,rot) = listener.lookupTransform('/base_link', '/marker_2_target', rospy.Time(0))
            (trans3,rot) = listener.lookupTransform('/base_link', '/marker_3_target', rospy.Time(0))

        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        
        print(trans1)
        print(trans2)
        print(trans3)
        print(" ")
        rate.sleep()

