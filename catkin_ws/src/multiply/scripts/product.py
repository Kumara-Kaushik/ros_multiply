#!/usr/bin/env python

import rospy
from multiply.msg import Num

class Multiply():
    def __init__(self, node_name):
        self.node_name = node_name

    def start(self):
        self.pub = rospy.Publisher('multiped_output', Num, queue_size=10)

    def multiply(self):
        a = int(input("Input first number: "))
        b = int(input("Input first number: "))
        product = a * b
        msg = Num()
        msg.num_a = a
        msg.num_b = b
        msg.product = product
        self.pub.publish(msg)

if __name__ == '__main__':
   rospy.init_node('multiply', anonymous=True)
   multiply_func = Multiply(node_name=rospy.get_name())
   multiply_func.start()
   rate = rospy.Rate(10) # 10hz

   while not rospy.is_shutdown():
        multiply_func.multiply()
        rate.sleep()