from skimage.metrics import structural_similarity as ssim
import numpy as np
import cv2
import json
import copy
import rospy

from std_msgs.msg import Float32,String

SSIM_THRESHOLD = 0.65
GRAD_THRESHOLD =0.65
VIDEO_NUMBER = 2
''' if you want to check port num
[bash]
ls -al /dev/video*
'''


#ros::Subscriber<std_msgs::String> close_flag("change", close_cb); // same/diff

class SSIM:
    def __init__(self):
        self.data = None #전역변수로 선언을 해주고
        self.grad = None
        self.state = None
        self.bookcase = None
        self.same = "same"
        rospy.init_node('ssim_pub_node', anonymous=True)
        self.publisher1 = rospy.Publisher('SSIM', Float32, queue_size=10)
        self.publisher2 = rospy.Publisher('GRAD', Float32, queue_size=10)
        self.publisher3 = rospy.Publisher('change', String,queue_size=10)
        self.subscriber1 = rospy.Subscriber(
            name='bookcase_state', data_class=String, callback=self.callbackFunction1)
        self.subscriber2 = rospy.Subscriber(
            name="bookcase_num", data_class=String, callback=self.callbackFunction2)
        self.rate = rospy.Rate(30) # 0.5hz

    def callbackFunction1(self,msg): #기본 argument는 구독한 메세지 객체 
        #callback : topic이 발행되는 이벤트가 발생하였을 때 event lisner함수를 콜백함수로 요구
        self.state = msg.data #받아서 상태 저장만
        

    def callbackFunction2(self,msg):
        self.bookcase = msg.data
        #rospy.loginfo(self.bookcase)

    def ssim_publish(self):
        if self.state == "open":
            self.publisher1.publish(self.data)
            #rospy.loginfo(self.data)
        else:
            self.publisher1.publish(0)
        self.rate.sleep() #100hz가 될때 까지 쉬기

    def diff_publish(self,current_score,past_score):
        # FPS 30 : 1/30000s -> 1frame
        sec = 1/30000
        if self.state == "open":
            self.grad = (abs((current_score-past_score)/sec)/1000)**2
            self.publisher2.publish(self.grad)
        else:
            self.publisher2.publish(0)
        self.rate.sleep() #100hz가 될때 까지 쉬기

    def change_publish(self):
        if self.same == "diff":
            self.publisher3.publish(self.same)
            #rospy.loginfo(self.data)
        else:
            pass
            #self.publisher3.publish(0)
        self.rate.sleep() #100hz가 될때 까지 쉬기


FPS = 30


cap = cv2.VideoCapture(VIDEO_NUMBER)
json_path = "../../config/ROI.json"



print("camera width : %d, camera height : %d" %(cap.get(cv2.CAP_PROP_FRAME_WIDTH) , cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

with open(json_path, "r") as json_file:
    ROI = json.load(json_file)



# ROI = {#(x,y) (x+w,y+h)
#             #left top, right bottom
#             #x : 0 ~ 1920 (left-right), y : 0 ~ 1080 (top -bottom)

#=======================================================================


flag = 0
flag_diff = 0
curr_cap =None
past_cap = None
past_bookcase_num = ""
s= SSIM()
my_lst = []

while cap.isOpened():
    _,src = cap.read()
    curr_cap = src.copy()

    bookcase_num = s.bookcase
    bookcase_num = "book2" #임시 나중에 빼기

    if past_bookcase_num == "" or past_bookcase_num != bookcase_num:
        print("ROI weigh : %d , height : %d " %( ROI[bookcase_num]['x2']-ROI[bookcase_num]['x1'] , ROI[bookcase_num]['y2']-ROI[bookcase_num]['y1']))
        past_bookcase_num = bookcase_num

    if flag == 0: # pass to one frame at starting point (need of past)
        flag = 1

    else:
        
        curr_crop = curr_cap[ROI[bookcase_num]['y1']: ROI[bookcase_num]['y2'], ROI[bookcase_num]['x1']:ROI[bookcase_num]['x2']]
        past_crop = past_cap[ROI[bookcase_num]['y1']: ROI[bookcase_num]['y2'], ROI[bookcase_num]['x1']:ROI[bookcase_num]['x2']]

        #cv2.rectangle(frame,left top, right bottom, color(RGB), Thickness(-1:filled))
        cv2.rectangle(src,(ROI[bookcase_num]['x1'],ROI[bookcase_num]['y1']),(ROI[bookcase_num]['x2'],ROI[bookcase_num]['y2']), (255,0,0),2)
        #hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

        #For use Compute SSIM (must convert for gray)
        curr_gray = cv2.cvtColor(curr_crop, cv2.COLOR_BGR2GRAY)
        past_gray = cv2.cvtColor(past_crop, cv2.COLOR_BGR2GRAY)


        #Globally
        #(score, diff) = ssim(grayA, grayB,full=True)

        #Locally
        (score, diff) = ssim(curr_gray, past_gray, win_size= 63 ,full=True)
        #(score, diff) = ssim(curr_gray, past_gray, win_size= 153 ,full=True)
        diff = (diff * 255).astype("uint8")
        
        curr_score = score
        if flag_diff ==0:
            flag_diff = 1 
            pass
        else:
            s.diff_publish(curr_score,past_score)

        past_score = curr_score

        s.data = score
        s.ssim_publish()


        thresh = cv2.threshold(
                diff, 0, 255,#200 
                cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU
            )[1]
        cnts, _ = cv2.findContours(
                    thresh, 
                    cv2.RETR_EXTERNAL, 
                    cv2.CHAIN_APPROX_SIMPLE
                    )

        for c in cnts:
            area = cv2.contourArea(c)
            if area > 40: #40
                x, y, w, h = cv2.boundingRect(c)
                # cv2.rectangle(src, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.rectangle(src, (x+ROI[bookcase_num]['x1'], y+ROI[bookcase_num]['y1']), (x + w+ROI[bookcase_num]['x1'], y + h+ROI[bookcase_num]['y1']), (0, 0, 255), 2)
                cv2.drawContours(curr_crop, [c], -1, (0, 0, 255), 2)
        past_bookcase_num = bookcase_num
        cv2.imshow("VideoFrame", src)
        cv2.imshow("contour",curr_crop)
    past_cap = src
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    if cv2.waitKey(int(1000/FPS)) & 0xFF == ord('q'): #FPS 30 =>  Time  = 1000 / FPS
        break

cv2.destroyAllWindows()