#! /usr/bin/env python
import rospy                                
rospy.init_node("hello_python_node")     
from time import sleep
n=1
while n<11:
    if n==10:
	sleep(1)
	print("time over")
	n+=1
    elif n<10:
	sleep(1)
	print(n)
	n+=1   
