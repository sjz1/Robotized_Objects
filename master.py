#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Point, Quaternion
import tf
from math import radians, copysign, sqrt, pow, pi, atan2
from tf.transformations import euler_from_quaternion
import numpy as np

class stool:

    # user_info="none"
    # shelf5_open=False
    # shelf6_open=False
    # shelf7_open=False
    # shelf8_open=False
    # shelf9_open=False
    turtlebot3_move=False
    # scenario1=False
    # scenario2=False
    # cnt_open=0
    # cnt_close=0
    #reset_cnt=0

    def __init__(self):
        rospy.Subscriber("height", String, self.callback1)
        #rospy.Subscriber("book", String, self.callback2)
        #rospy.Subscriber("shelf_close", String, self.callback3)

        rospy.on_shutdown(self.shutdown)
        self.cmd_vel = rospy.Publisher('cmd_vel', Twist, queue_size=5)
        position = Point()
        move_cmd = Twist()
        r = rospy.Rate(10)
        self.tf_listener = tf.TransformListener()
        self.odom_frame = 'odom'

        #self.stool_pos()

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
            self.movebase_client(0.2,0,0)
            stool.turtlebot3_move=False  
        
        elif data.data =="scenario1":
            stool.turtlebot3_move=True   
            self.movebase_client(0,0,0)
            stool.turtlebot3_move=False

        elif data.data =="scenario2":
            stool.turtlebot3_move=True   
            self.movebase_client(0,0,0)
            stool.turtlebot3_move=False    

        

        elif data.data =="test1":
            #if stool.reset_cnt==0:
                #stool.turtlebot3_move=True   
                #for i in [1,2]:
                    #if i == 1:
                        #self.movebase_client(1.6,0,-90)
                    #elif i ==2:
                        #self.movebase_client(1.6,-0.6,0)
            self.movebase_client(1.6,-0.85,0)
            stool.turtlebot3_move=False
                # stool.reset_cnt=stool.reset_cnt+1 
	#시나리오: 1번 갔다가 3번
        elif data.data =="test2":
            #if stool.reset_cnt==0:
            stool.turtlebot3_move=True   
            self.movebase_client(0,0,0)
            stool.turtlebot3_move=False

        elif data.data =="test3":
            # if stool.reset_cnt==0:
            stool.turtlebot3_move=True   
            self.movebase_client(0.85,-1,0)
            stool.turtlebot3_move=False

        elif data.data =="test4":
            #if stool.reset_cnt==0:
            stool.turtlebot3_move=True   
            self.movebase_client(0.6,-0.35,0)
            stool.turtlebot3_move=False
	#2번 시나리오: 2번, 4번
    
       
        elif data.data =="test5":
            #if stool.reset_cnt==0:
                stool.turtlebot3_move=True   
                self.movebase_client(1.5,-0.7,0)
                stool.turtlebot3_move=False

        

        # elif data.data == "check":
        #     print("user info: %s" %stool.user_info)
        #     print("shelf5_open: %d" %stool.shelf5_open)
        #     print("shelf6_open: %d" %stool.shelf6_open)
        #     print("shelf7_open: %d" %stool.shelf7_open)
        #     print("shelf8_open: %d" %stool.shelf8_open)
        #     print("shelf9_open: %d" %stool.shelf9_open)
        #     print("turtlebot3_move: %d" %stool.turtlebot3_move)
        #     print("scenario1: %d" %stool.scenario1)
        #     print("scenario2: %d" %stool.scenario2)
        #     print("cnt_open: %d" %stool.cnt_open)
        #     print("cnt_close: %d" %stool.cnt_close)
        #     print("reset_cnt: %d" %stool.reset_cnt)


            
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
                     self.movebase_client(1.8,-1.5,135)
                     # result = self.movebase_client(1.8,-1.2,-180)
                     # if result:
                     #     rospy.loginfo("Stool arrived in front of shelf6!")
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
                     if stool.reset_cnt==0:
                         stool.turtlebot3_move=True   
                         for i in [1,2]:
                             if i == 1:
                                 self.movebase_client(0.4,-1.2,90)
                             elif i ==2:
                                 self.movebase_client(0.8,-1.4,135)
                         stool.turtlebot3_move=False
                         stool.reset_cnt=stool.reset_cnt+1
                     stool.cnt_open=0

                 if stool.cnt_close ==4:
                     stool.turtlebot3_move=True
                     self.movebase_client(0.3,-0.5,0)
                     stool.turtlebot3_move=False
                     stool.cnt_close=0
            
    def movebase_client(self,x,y,z):
        rospy.on_shutdown(self.shutdown)
        self.cmd_vel = rospy.Publisher('cmd_vel', Twist, queue_size=5)
        position = Point()
        move_cmd = Twist()
        r = rospy.Rate(10)
        self.tf_listener = tf.TransformListener()
        self.odom_frame = 'odom'
        try:
            self.tf_listener.waitForTransform(self.odom_frame, 'base_footprint', rospy.Time(), rospy.Duration(1.0))
            self.base_frame = 'base_footprint'
        except (tf.Exception, tf.ConnectivityException, tf.LookupException):
            try:
                self.tf_listener.waitForTransform(self.odom_frame, 'base_link', rospy.Time(), rospy.Duration(1.0))
                self.base_frame = 'base_link'
            except (tf.Exception, tf.ConnectivityException, tf.LookupException):
                rospy.loginfo("Cannot find transform between odom and base_link or base_footprint")
                rospy.signal_shutdown("tf Exception")

        (position, rotation) = self.get_odom()
        last_rotation = 0
        linear_speed = 1
        angular_speed = 1
        (goal_x, goal_y, goal_z) = [float(x), float(y), float(z)]
        if goal_z > 180 or goal_z < -180:
            print("you input wrong z range.")
            self.shutdown()
        goal_z = np.deg2rad(goal_z)
        goal_distance = sqrt(pow(goal_x - position.x, 2) + pow(goal_y - position.y, 2))
        distance = goal_distance

       
        while distance > 0.05:
            (position, rotation) = self.get_odom()
            x_start = position.x
            y_start = position.y
            path_angle = atan2(goal_y - y_start, goal_x- x_start)
            
            if path_angle < -pi/4 or path_angle > pi/4:
                if goal_y < 0 and y_start < goal_y:
                    path_angle = -2*pi + path_angle
                elif goal_y >= 0 and y_start > goal_y:
                    path_angle = 2*pi + path_angle

            if last_rotation > pi-0.1 and rotation <= 0:
                rotation = 2*pi + rotation
            elif last_rotation < -pi+0.1 and rotation > 0:
                rotation = -2*pi + rotation
            move_cmd.angular.z = angular_speed * path_angle-rotation

            distance = sqrt(pow((goal_x - x_start), 2) + pow((goal_y - y_start), 2))
            move_cmd.linear.x = min(linear_speed * distance, 0.1)*1.2
            #move_cmd.linear.x = 0.1
            
            
            if move_cmd.angular.z > 0:
                move_cmd.angular.z = min(move_cmd.angular.z, 1.5)
            else:
                move_cmd.angular.z = max(move_cmd.angular.z, -1.5)

            last_rotation = rotation
            self.cmd_vel.publish(move_cmd)
            r.sleep()
        (position, rotation) = self.get_odom()

        while abs(rotation - goal_z) > 0.05:
            (position, rotation) = self.get_odom()
            if goal_z >= 0:
                if rotation <= goal_z and rotation >= goal_z - pi:
                    move_cmd.linear.x = 0.00
                    move_cmd.angular.z = 0.5
                else:
                    move_cmd.linear.x = 0.00
                    move_cmd.angular.z = -0.5
            else:
                if rotation <= goal_z + pi and rotation > goal_z:
                    move_cmd.linear.x = 0.00
                    move_cmd.angular.z = -0.5
                else:
                    move_cmd.linear.x = 0.00
                    move_cmd.angular.z = 0.5
            self.cmd_vel.publish(move_cmd)
            r.sleep()


        self.cmd_vel.publish(Twist())

    def get_odom(self):
        try:
            (trans, rot) = self.tf_listener.lookupTransform(self.odom_frame, self.base_frame, rospy.Time(0))
            rotation = euler_from_quaternion(rot)

        except (tf.Exception, tf.ConnectivityException, tf.LookupException):
            rospy.loginfo("TF Exception")
            return

        return (Point(*trans), rotation[2])


    def shutdown(self):
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)    

if __name__ == '__main__':
	
        rospy.init_node('stool', anonymous=False)
        stool()
        rospy.spin()
