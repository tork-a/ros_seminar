#!/usr/bin/env python
#coding:utf-8

from moveit_commander import MoveGroupCommander
from geometry_msgs.msg import Pose, Point, Quaternion
import rospy, time, tf, os, math, numpy
from dynamixel_controllers.srv import *


def pick_and_place(pick_trans, place_trans):
    Clearance = 0.030
    Offset = 0.040
    
    tmpth = math.atan2(pick_trans[1], pick_trans[0])
    move_arm([pick_trans[0] - Offset*math.cos(tmpth), pick_trans[1] - Offset*math.sin(tmpth), pick_trans[2]])
    set_slope(32)
    move_arm([pick_trans[0], pick_trans[1], pick_trans[2]])
    set_slope(64)
    move_arm([pick_trans[0], pick_trans[1], place_trans[2]+Clearance])
    move_arm([place_trans[0], place_trans[1], place_trans[2]+Clearance])
    set_slope(32)
    move_arm([place_trans[0], place_trans[1], place_trans[2]])
    set_slope(64)
    tmpth = math.atan2(place_trans[1], place_trans[0])
    move_arm([place_trans[0] - Offset*math.cos(tmpth), place_trans[1] - Offset*math.sin(tmpth), place_trans[2]])


def move_arm(target_position):
    target_orientation = Quaternion(*tf.transformations.quaternion_from_euler(0.0, 1.5, math.atan2(target_position[1], target_position[0]), 'sxyz'))
    target_pose = Pose(Point(*target_position), target_orientation)
    group.set_pose_target(target_pose)
    print("Target Pose:")
    print(target_pose)
    plan = group.plan()
    if len(plan.joint_trajectory.points) == 0:
        print("No plan found. exitting...")
        sys.exit()
    group.go()
    #group.execute(plan)
    time.sleep(1)


def set_slope(sl):
        print("Changing Dynamixel Compliance Slope to %d..." % sl)
        try:
            controllers = ['/base_lift_controller','/base_pan_controller','/elbow_flex_controller','/wrist_flex_controller']
            for controller in controllers:
                set_compliance_slope = rospy.ServiceProxy(controller + '/set_compliance_slope', SetComplianceSlope)
                temp = set_compliance_slope(sl)
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e
    
    
def arm_demo():            
    rospy.init_node("marker_demo")
    
    listener = tf.TransformListener()
    rate = rospy.Rate(10.0)
    gonow = 0
    cnt = 0
    trans_stack = numpy.zeros((10,6)) #10 lines of x1,y1,x2,y2,x3,y3
    
    print('Hit RETURN key when you are ready.')
    raw_input()
    
    while not gonow and not rospy.is_shutdown():
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
        #check stability
        trans_stack[cnt,0:2] = trans1[0:2]
        trans_stack[cnt,2:4] = trans2[0:2]
        trans_stack[cnt,4:6] = trans3[0:2]
        cnt = cnt + 1
        if cnt == 10:
            gonow = 1
            for i in range(6):
                if 0.001 < abs(max(trans_stack[:,i])-min(trans_stack[:,i])):
                    gonow = 0
            if gonow == 1:
                avg_trans = numpy.zeros([3,2])
                for i in range(3):
                    for j in range(2):
                        avg_trans[i,j] = numpy.mean(trans_stack[:,i*2+j])
            else:
                cnt = 0
                trans_stack = numpy.zeros((10,6))
                print("retry detection; markers offset is too large.") 
        rate.sleep()
    
    print("averaged trans")
    print(avg_trans)
    
    #sort by distance
    mark_dis = [0,0,0]
    for i in range(3):
        mark_dis[i] = numpy.linalg.norm(avg_trans[i,:])
    sorted_ix = sorted(range(len(mark_dis)), key=lambda k: mark_dis[k])
 
    pick_trans1 = avg_trans[sorted_ix[0],:]
    pick_trans2 = avg_trans[sorted_ix[1],:]
    place_trans = avg_trans[sorted_ix[2],:]
    
    set_slope(64)
    PackThickness = 0.026
    PickHight = 0.022
    
    #start manipulation
    pick_and_place([pick_trans1[0], pick_trans1[1], PickHight], [place_trans[0], place_trans[1], PickHight+PackThickness])
    pick_and_place([pick_trans2[0], pick_trans2[1], PickHight], [place_trans[0], place_trans[1], PickHight+PackThickness*2])

    move_arm([0.05, 0.0, 0.24])


if __name__ == '__main__':
    try:
        group = MoveGroupCommander("whole_arm")
        arm_demo()
    except rospy.ROSInterruptException:
        pass
