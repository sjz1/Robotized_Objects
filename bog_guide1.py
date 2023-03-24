#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import String

class stool:

    user_info="none"
    shelf5_open=False
    shelf6_open=False
    shelf7_open=False
    shelf8_open=False
    shelf9_open=False
    turtlebot3_move=False
    scenario1=False
    scenario2=False
    cnt_open=0
    cnt_close=0

    def __init__(self):
        rospy.Subscriber("height", String, self.callback1)
        rospy.Subscriber("book", String, self.callback2)
        rospy.Subscriber("shelf_close", String, self.callback3)
        self.stool_pos()

    def callback1(self, data):

        if data.data == "adult":
            stool.user_info = "adult"
            stool.scenario2=True
            print(stool.user_info)
            rospy.loginfo("I heard user is  %s", stool.user_info)
          
        elif data.data == "child":
            stool.user_info = "child"
            print(stool.user_info)
            rospy.loginfo("I heard user is  %s", stool.user_info)
        
        elif data.data == "reset":
            stool.user_info = "none"
            rospy.loginfo("I heard user is  %s", stool.user_info)

        elif data.data =="sit":
            stool.turtlebot3_move=True   
            result = self.movebase_client(0.5,0,0)
            if result:
                rospy.loginfo("Have a sit!")
                stool.turtlebot3_move=False  

        elif data.data =="bye":
            stool.turtlebot3_move=True   
            result = self.movebase_client(0,0,0)
            if result:
                rospy.loginfo("Good bye!")
                stool.turtlebot3_move=False  

        elif data.data == "check":
            print("user info: %s" %stool.user_info)
            print("shelf5_open: %d" %stool.shelf5_open)
            print("shelf6_open: %d" %stool.shelf6_open)
            print("shelf7_open: %d" %stool.shelf7_open)
            print("shelf8_open: %d" %stool.shelf8_open)
            print("shelf9_open: %d" %stool.shelf9_open)
            print("turtlebot3_move: %d" %stool.turtlebot3_move)
            print("scenario1: %d" %stool.scenario1)
            print("scenario2: %d" %stool.scenario2)
            print("cnt_open: %d" %stool.cnt_open)
            print("cnt_close: %d" %stool.cnt_close)

            
    def callback2(self, data):
        
        if data.data == "shelf5":
            if stool.scenario2==True:
                stool.cnt_open=stool.cnt_open+1
            stool.shelf5_open=True
            #print(stool.shelf5_open)
            rospy.loginfo("shelf5 opening")
        
        elif data.data == "shelf6":
            if stool.scenario2==True:
                stool.cnt_open=stool.cnt_open+1
            stool.shelf6_open=True
            #print(stool.shelf6_open)
            rospy.loginfo("shelf6 opening")
        
        elif data.data == "shelf7":
            if stool.scenario2==True:
                stool.cnt_open=stool.cnt_open+1
            stool.shelf7_open=True
            #print(stool.shelf7_open)
            rospy.loginfo("shelf7 opening")
        
        elif data.data == "shelf8":
            if stool.scenario2==True:
                stool.cnt_open=stool.cnt_open+1
            stool.shelf8_open=True
            #print(stool.shelf8_open)
            rospy.loginfo("shelf8 opening")
        
        elif data.data == "shelf9":
            if stool.scenario2==True:
                stool.cnt_open=stool.cnt_open+1
            stool.shelf9_open=True
            #print(stool.shelf9_open)
            rospy.loginfo("shelf9 opening")
    
    def callback3(self, data):

        if data.data == "shelf5_close":
            if stool.scenario2==True:
                stool.cnt_close=stool.cnt_close+1
            stool.shelf5_open=False
            #print(stool.shelf5_open)
            rospy.loginfo("shelf5 closing")
        
        elif data.data == "shelf6_close":
            if stool.scenario2==True:
                stool.cnt_close=stool.cnt_close+1
            stool.shelf6_open=False
            #print(stool.shelf6_open)
            rospy.loginfo("shelf6 closing")
        
        elif data.data == "shelf7_close":
            if stool.scenario2==True:
                stool.cnt_close=stool.cnt_close+1
            stool.shelf7_open=False
            #print(stool.shelf7_open)
            rospy.loginfo("shelf7 closing")
        
        elif data.data == "shelf8_close":
            if stool.scenario2==True:
                stool.cnt_close=stool.cnt_close+1
            stool.shelf8_open=False
            #print(stool.shelf8_open)
            rospy.loginfo("shelf8 closing")
        
        elif data.data == "shelf9_close":
            if stool.scenario2==True:
                stool.cnt_close=stool.cnt_close+1
            stool.shelf9_open=False
            #print(stool.shelf9_open)
            rospy.loginfo("shelf9 closing")


    def stool_pos(self):
        while 1:
            #print("check1")
            if stool.user_info =="child" :
                #print("check2")
                if stool.shelf6_open==True:
                    #print("check3")
                    stool.turtlebot3_move=True
                    stool.scenario1=True
                    result = self.movebase_client(1.6, -1.6 ,0)
                    if result:
                        rospy.loginfo("Stool arrived in front of shelf6!")
                        stool.turtlebot3_move=False
                else:
                    if stool.scenario1==True:
                        stool.turtlebot3_move=True
                        result = self.movebase_client(0,0,0)
                        if result:
                            rospy.loginfo("Stool arrived in front of table!")
                            stool.turtlebot3_move=False
                            stool.scenario1=False

            elif stool.user_info=="adult":
                if stool.cnt_open >=3:
                    stool.turtlebot3_move=True
                    result = self.movebase_client(1.6,0.8,0)
                    if result:
                        rospy.loginfo("Stool arrived in front of shelf7!")
                        stool.turtlebot3_move=False
                        stool.cnt_open=0
                if stool.cnt_close ==4:
                    stool.turtlebot3_move=True
                    result = self.movebase_client(0,0,0)
                    if result:
                        rospy.loginfo("Stool arrived in front of other stool!")
                        stool.turtlebot3_move=False
                        stool.cnt_close=0
            
    def movebase_client(self,x,y,z):

        client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        client.wait_for_server()

        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = x
        goal.target_pose.pose.position.y = y
        goal.target_pose.pose.orientation.z = z
        goal.target_pose.pose.orientation.w = 1.0

        client.send_goal(goal)

	    #return 1
        wait = client.wait_for_result()
        if not wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
        	return client.get_result()

if __name__ == '__main__':

        rospy.init_node('stool', anonymous=False)
        stool()
        rospy.spin()
