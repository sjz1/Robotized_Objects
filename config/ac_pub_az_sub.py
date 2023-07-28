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
from std_msgs.msg import Float32, String


class height:
    def __init__(self):
        rospy.init_node('az_sub_ac_pub_node', anonymous=True)
        self.data = None #전역변수로 선언을 해주고
        self.height_threshold = rospy.get_param('~height_threshold')
        self.ac = None
        self.subscriber = rospy.Subscriber(
            name="length", data_class=Float32, callback=self.callbackFunction)
        self.publisher = rospy.Publisher('ac_information', String, queue_size=10)
        self.rate = rospy.Rate(30) # 0.5hz


    def callbackFunction(self,msg): #기본 argument는 구독한 메세지 객체 
        #callback : topic이 발행되는 이벤트가 발생하였을 때 event lisner함수를 콜백함수로 요구
        self.data = msg
        #rospy.loginfo(type(data))
        #rospy.loginfo(int(data))
        #rospy.loginfo(int(msg.data))
        if int(msg.data) == 0:
            rospy.loginfo("사람이 인식되지 않음")
            self.ac = "None"
        elif int(msg.data) >= self.height_threshold:
            rospy.loginfo("adult")
            self.ac = "adult"
        else:
            rospy.loginfo("child")
            self.ac = "child"
        rospy.loginfo(self.ac)
        self.publisher.publish(self.ac)
        #rospy.loginfo("ac_publisher action")
        


    def acpub_azsub_action(self):
        while not rospy.is_shutdown(): #-> c++에서 ros.ok() 느낌
            #rospy.loginfo(rospy.get_time())
            self.rate.sleep() #100hz가 될때 까지 쉬기

            




if __name__ == '__main__':
    try:
        h = height()
        h.acpub_azsub_action()
    except rospy.ROSInterruptException:
        pass
