#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import String

class stool:

    user_info="none"
    #시나리오 
    shelf5_open=False
    #각 서랍 
    turtlebot3_move=False
    scenario1=False
    scenario2=False
    cnt_open=0
    #서랍이 열린 횟수
    cnt_close=0
    #서랍이 닫힌 횟수

    def __init__(self):
        rospy.Subscriber("height", String, self.callback1)
        rospy.Subscriber("book", String, self.callback2)
        rospy.Subscriber("shelf_close", String, self.callback3)   
        self.stool_pos()

    def callback1(self, data):     
    #이건 키에서 오는 height 값 (아두이노에서 sensor1, sensor2로 센싱)

        if data.data == "adult":
            stool.user_info = "adult" 
            #stool.user_info라는 변수를 adult라고 둠 앞에 stool이 붙은 건 class명 때문 
            stool.scenario2=True      #stool.scenario2라는 변수는 true라고 두어 adult이다. 
            print(stool.user_info)    
            rospy.loginfo("I heard user is  %s", stool.user_info)
            
          
        elif data.data == "child":
            stool.user_info = "child" #stool.user_info라는 변수를 adult라고 둠
            print(stool.user_info)
            rospy.loginfo("I heard user is  %s", stool.user_info)
        
        elif data.data == "reset":
            stool.user_info = "none"
            rospy.loginfo("I heard user is  %s", stool.user_info)
            
                
        #임의로 data 값이 sit, bye로 들어오면 의자를 이동시켜 줌. 

  

            
    def callback2(self, data):    #self 값은 다른 def에서도 해당 변수가 이어짐을 의미
        
        if data.data == "book5":
            if stool.scenario2==True:
                stool.cnt_open=stool.cnt_open+1
            #shelf5라고 한다면 stool.scenario2가 false에서 true이 되고 
            #cnt_open 값은 1이 더해져서 1이 됨.
            stool.shelf5_open=True
            rospy.loginfo("shelf5 opening")
            
            #shelf5라고 한다면 stool.scenario2가 false에서 true이 됨. 
            #cnt_open 값은 1이 더해져서 1이 됨. -> callback3에서 
            #stool.shelf5_open도 true가 됨. 
        
    
    def callback3(self, data):

        if data.data == "reset5":
            if stool.scenario2==True:
                stool.cnt_close=stool.cnt_close+1
            stool.shelf5_open=False
            
            #반대로 닫히는 거 
            #scenario2는 callback2에서 True가 되었으니 if문은 참값->
            #stool.cnt_close 값은 1이 더해짐.  
            #shelf5_open 값은 거짓
    


    def stool_pos(self):
        while 1:
            if stool.user_info =="child" :
            #어린이 시나리오일 경우
                if stool.shelf5_open==True:
                #callback2에서 받는 데이터가 맞다면 서랍이 열렸으니 True일 수 밖에 없음. 
                #이 때는 시나리오이다보니 특정 서랍을 열어줬을 때 열리도록 하였음. 
                #만약 임의의 서랍을 열었을 때 작동되도록 하려면 
                #if stool.cnt_open >=1:
                #을 쓰면 됨 
                    stool.turtlebot3_move=True
                    #turtlebot3_move가 True 값이 되고 
                    stool.scenario1=True
                    #scenario1도 True
                    result = self.movebase_client(1.6, -1.6 ,0)
                    #movebase_client 함수를 활용
                    if result:
                        rospy.loginfo("Stool arrived in front of shelf6!")
                        stool.turtlebot3_move=False
                    #result 변수가 실행 되고 나면 (즉 터틀봇이 이동하고 나면)
                    #turtlebot3_move는 false가 된다. 
                else:
                #stool.shelf5_open이 false라면
                #즉, callback3으로 받는 data값이 
                    if stool.scenario1==True:
                    #scenario1이 if 문에서 True가 되었으니
                    #if stool.scenario1이 참값이 되야 한다.
                    #callback3에서 받는 데이터가 맞다면 서랍이 닫혔으니 False일 수 밖에 없음. 
                        stool.turtlebot3_move=True
                        result = self.movebase_client(0,0,0)
                        if result:
                            rospy.loginfo("Stool arrived in front of table!")
                            stool.turtlebot3_move=False
                            stool.scenario1=False
                            #scenario1은 잠굼 - 두번째 if, else 문을 잠가버림. 

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
       #movebase_client의 경우 turtlebot emanual에서 함수 가져옴

if __name__ == '__main__':

        rospy.init_node('stool', anonymous=False)
        stool()
        rospy.spin()
        #stool이라는 클래스를 그대로 실행
        
