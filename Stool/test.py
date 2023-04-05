#!/usr/bin/env python
# license removed for brevity

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import String
global mode_str



def keyboard():
    while 1:
        key_input = input("What place do you want? (1/2/3/4): ")
        if key_input == 1:
            print("Send message : you choose '1'")
            movebase_client(1.7, -1.7 ,0)
            print("Send message : go '1'")
            break
        elif key_input == 2:
            mode_str = "2"
            print("Send message : you choose '2'")
            movebase_client(0.2, -0.4 ,0)
            print("Send message : go '2'")
            break
        elif key_input == 3:
            mode_str = "3"
            print("Send message : you choose '3'")
            movebase_client(0.2, -0.3 ,0)
            print("Send message : go '3'")
            break
        elif key_input == 4:
            mode_str = "4"
            print("Send message : you choose '4'")
            movebase_client(0, 0 ,0)
            print("Send message : go '4'")
            break
            
def movebase_client(x,y,z):

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
    rospy.init_node('movebase_client')
    try:
        while 1:
            keyboard()
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")