#!/usr/bin/env python3
#-*- coding:utf-8 -*-	# 한글 주석을 달기 위해 사용한다.


''' azure에서 보내는 publish 정보
        std_msgs::Float32 msg;
        msg.data = 0;
        pub.publish(msg);

TrackerNode::TrackerNode(ros::NodeHandle& _nh)
{
	nh=_nh;
	lengthPub = nh.advertise<std_msgs::Float32>("length",1000);	
}


OpenCR 에서 보내는 정보     

ros::Publisher sceinaro_make("bookcase_num",  &moter_num)
std_msgs::String moter_num //string type으로 bookcase_num topic날림

'''

import rospy
from std_msgs.msg import Float32, String, Int32
from datetime import datetime

now = datetime.now()

class monitor:
    def __init__(self):
        rospy.init_node('monitoring_node', anonymous=True)

        self.flag = -1

        ###############################
        ####### Make Subscriber #######
        ###############################

        #             [length,adult/child,bookcase_num,count,sceinaro]
        self.status = [None, None,        None,         None,    None]

        self.length_subscriber = rospy.Subscriber(
            name="length", data_class=Float32, callback=self.length_callback)

        self.ac_subscriber = rospy.Subscriber(
            name="ac_information", data_class=String, callback=self.ac_callback)

        self.bookcase_subscriber = rospy.Subscriber(
            name="bookcase_num", data_class=String, callback=self.bookcase_callback)
        
        self.count_subscriber = rospy.Subscriber(
            name="count", data_class=Int32, callback=self.count_callback)

        self.count_subscriber = rospy.Subscriber(
            name='sceinaro_num', data_class=String, callback=self.sceinaro_callback)

        self.rate = rospy.Rate(30) # 0.5hz

    def length_callback(self,msg): #기본 argument는 구독한 메세지 객체
        #callback : topic이 발행되는 이벤트가 발생하였을 때 event lisner함수를 콜백함수로 요구
        state_idx = 0
        self.status[state_idx] = msg.data  #length는 매번 바뀐다고 생각하였다


    def ac_callback(self,msg): #ac를 인식하는 부분
        state_idx = 1

        if self.status[state_idx] == None: 
            pass

        else: #무언가가 있을때
            if self.status[state_idx] == msg.data: #같은게 들어왔을 때
                pass

            else: #다른게 들어왔을때
                self.status[state_idx] = msg.data #갱신
                self.flag = state_idx #플래그 올리고

        self.status[state_idx] = msg.data #update

    def bookcase_callback(self,msg):
        state_idx = 2

        if self.status[state_idx] == None: 
            pass

        else: #무언가가 있을때
            if self.status[state_idx] == msg.data: #같은게 들어왔을 때
                pass

            else: #다른게 들어왔을때
                self.status[state_idx] = msg.data #갱신
                self.flag = state_idx #플래그 올리고

        self.status[state_idx] = msg.data #update


    def count_callback(self,msg):
        state_idx = 3

        if self.status[state_idx] == None: 
            pass

        else: #무언가가 있을때
            if self.status[state_idx] == msg.data: #같은게 들어왔을 때
                pass

            else: #다른게 들어왔을때
                self.status[state_idx] = msg.data #갱신
                #self.flag = state_idx #플래그 올리고

        self.status[state_idx] = msg.data #update


    def sceinaro_callback(self,msg):
        state_idx = 4

        #              [length , adult/child , bookcase_num , count , sceinaro]
        #self.status = [None ,  None ,         None ,          None ,     None]
        if self.status[state_idx] == None: # ac_information = None (초기상태)
            pass

        else: #무언가가 있을때
            if self.status[state_idx] == msg.data: #같은게 들어왔을 때 (ex : 1 -> 1)
                pass

            else: #다른게 들어왔을때
                self.status[state_idx] = msg.data #갱신 (ex : 1 -> 2)
                self.flag = state_idx #플래그 올리고

        self.status[state_idx] = msg.data #update


    def print_info(self,idx):
        state_name =   ["length" , "adult/child" , "bookcase_num" , "count" , "sceinaro"]
        rospy.loginfo("############### [Info] ####################")
        rospy.loginfo("## The %s is currently change ! ##" %state_name[idx])
        rospy.loginfo("## State Change occur in %s ##" %str(now.time()))
        rospy.loginfo("########################################### \n") 

        rospy.loginfo("########################")
        rospy.loginfo("## length : %s " %str(int(self.status[0])))
        rospy.loginfo("## ac_info : %s " %self.status[1])
        rospy.loginfo("## Book : %s " %self.status[2])
        rospy.loginfo("## count : %s " %str(self.status[3]))
        rospy.loginfo("## sceinaro : %s " %str(self.status[4]))
        rospy.loginfo("######################## \n\n\n")
        


    def Monitoring(self):
        while not rospy.is_shutdown(): #-> c++에서 ros.ok() 느낌
            
            #추후 이용하면 좋을 듯
            #rospy.loginfo(self.status)
            if self.flag == -1:
                pass
            else:
                self.print_info(self.flag)
                self.flag = -1
            self.rate.sleep() #100hz가 될때 까지 쉬기
            


if __name__ == '__main__':
    try:
        info = monitor()
        rospy.loginfo("#############################################################################")
        rospy.loginfo("##                                                                         ##")
        rospy.loginfo("##       ####    ####     ##  ##     ##     #####     ####    ########     ##")
        rospy.loginfo("##     ##      ##    ##   ##  ##   ##  ##   ##  ##  ##    ##     ##        ##")
        rospy.loginfo("##    ##      ##      ##  ##  ##  ########  #####  ##      ##    ##        ##")
        rospy.loginfo("##     ##      ##    ##   ##  ##  ##    ##  ##  ##  ##    ##     ##        ##")
        rospy.loginfo("##       ####    ####     ##  ##  ##    ##  #####     ####       ##        ##")
        rospy.loginfo("##                                                                         ##")
        rospy.loginfo("############################################################################# \n\n") 
        info.Monitoring()
    except rospy.ROSInterruptException:
        pass