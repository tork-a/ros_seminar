
#!/usr/bin/env python
 
import rospy
from std_msgs.msg import Float64
from leap_motion.msg import leap
from leap_motion.msg import leapros
 
pub = rospy.Publisher("/temp_controller/command", Float64)
 
def callback(data):	
    hnum = (data.palmpos.y - 200)/100*1.57
    pub.publish(hnum)    	
 
def send_command():
    rospy.init_node("leap_to_dynamixel")
    rospy.Subscriber("leapmotion/data", leapros, callback)
    rospy.spin()
   
if __name__ == '__main__':
    send_command()

