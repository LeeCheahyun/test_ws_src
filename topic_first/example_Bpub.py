#! /usr/bin/env python3
import rospy
from std_msgs.msg import String

def fun():
    pass

if __name__ == '__main__':
    rospy.init_node('sample_Bpub')
    pub = rospy.Publisher('helloB', String, queue_size=10)

    rate = rospy.Rate(10)
    # while True:    
    while not rospy.is_shutdown():
        str = "hello_publisher : %s " % rospy.get_time()
        pub.publish(str)
        rate.sleep()
    pass