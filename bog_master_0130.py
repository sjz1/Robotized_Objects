#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

import os

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def master():
    pub_cup_number = rospy.Publisher('table_mode', String, queue_size=10)
    rospy.init_node('master', anonymous=True)
    rate = rospy.Rate(10)
    #while not rospy.is_shutdown():
        #print("Will you continue? (yes : press anykey /no : press ESC)")
	#if getch() == chr(0x1b):
	    #break
	#while 1:
	    #cup_number = raw_input("What number do you want? (1/2): ")
	    #if cup_number == "1":
		
		    #mode_str = "1"
		    #rospy.loginfo(mode_str)
		    #pub_cup_number.publish(mode_str)
		    #rate.sleep()
		    #print("Send message : you choose '1'")
		    #break
	   
	    #elif cup_number == "2":
		    #mode_str = "2"
		    #rospy.loginfo(mode_str)
		    #pub_cup_number.publish(mode_str)
		    #rate.sleep()
		    #print("Send message : you choose '2'")
                    #break
	    
	    #else:
		    #print("You write a wrong answer. Please press 'r'")
		    #break


    while 1:
	cup_number = raw_input("What number do you want? (1/2): ")
	if cup_number == "1":
		
		mode_str = "1"
		rospy.loginfo(mode_str)
		pub_cup_number.publish(mode_str)
		rate.sleep()
		print("Send message : you choose '1'")
		
	   
        elif cup_number == "2":
		mode_str = "2"
		rospy.loginfo(mode_str)
		pub_cup_number.publish(mode_str)
		rate.sleep()
		print("Send message : you choose '2'")
                
	   
	else:
	        print("You write a wrong answer. Please press 'r'")
		break

	    	

if __name__ == '__main__':
    try:
        master()
    except rospy.ROSInterruptException:
        pass
