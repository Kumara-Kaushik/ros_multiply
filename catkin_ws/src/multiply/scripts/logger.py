#!/usr/bin/env python
import rospy
from multiply.msg import Num

def callback(data):
    a, b, product = data.num_a, data.num_b, data.product
    rospy.loginfo("Inputs: {} and {}, Multiplied Output: {}".format(a, b, product))

def logger():

    rospy.init_node('logger', anonymous=True)

    rospy.Subscriber("multiped_output", Num, callback)

    rospy.spin()

if __name__ == '__main__':
    logger()