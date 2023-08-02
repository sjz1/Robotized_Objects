from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import cv2
import rospy
from std_msgs.msg import Float32,String
import numpy as np
import time
import argparse

parser = argparse.ArgumentParser(description='Program for Graph (mode : SSIM/GRAD)')
parser.add_argument('--mode',help= "Select GRAD or SSIM(default = 'GRAD')",default = 'GRAD')
SSIM_THRESHOLD = 0.65
GRAD_THRESHOLD = 0.65
parser.add_argument('--ST',help= "SSIM Threshold(default = developer setting)",default = 'DEV')
parser.add_argument('--GT',help= "GRAD Threshold(default = developer setting))",default = 'DEV')

args = parser.parse_args() #

if args.ST != 'DEV':
    SSIM_THRESHOLD = args.ST

if args.GT != 'DEV':
    GRAD_THRESHOLD = args.GT


score = None #전역변수로 선언을 해주고
state = None
grad = None
FPS = 30

class graph:
    def __init__(self):
        rospy.init_node('ssim_sub_node', anonymous=True)
        self.subscriber1 = rospy.Subscriber(
            name="SSIM", data_class=Float32, callback=self.callbackFunction1)
        #ros::Publisher bookcase_state("bookcase_state",  &state);
        self.subscriber2 = rospy.Subscriber(
            name="bookcase_state", data_class=String, callback=self.callbackFunction2)
        self.subscriber = rospy.Subscriber(
            name="GRAD", data_class=Float32, callback=self.callbackFunction3)
        self.rate = rospy.Rate(30) # 0.5hz

    def callbackFunction1(self,msg): #기본 argument는 구독한 메세지 객체 
        global score
        score = float(msg.data)
        self.rate.sleep() #100hz가 될때 까지 쉬기

    def callbackFunction2(self,msg): #기본 argument는 구독한 메세지 객체 
        global state
        state = msg.data
        self.rate.sleep() #100hz가 될때 까지 쉬기

    def callbackFunction3(self,msg): #기본 argument는 구독한 메세지 객체 
        global grad
        grad = float(msg.data)
        self.rate.sleep() #100hz가 될때 까지 쉬기

g = graph()

# #그래프 정보 설정
# plt.tight_layout()
#plt.xlabel('time') #x 라벨
#plt.ylabel('Score') #y 라벨
#plt.title("SSIM") #그래프 이름

graph_x = np.array([])
graph_y = np.array([])
index = count()

    
fig = plt.figure()
ax = plt.axes(xlim=(30, 500), ylim=(0.3, 1))
line, = ax.plot([], [], lw=3)


def animate(i):
  global score 
  global graph_x
  global graph_y
  global state 
  global grad
  if state != "open":
      score,grad = 0,0
  graph_x = np.append(graph_x,next(index))
  graph_y = np.append(graph_y,score)
  line.set_data(graph_x, graph_y)
  return line,


#그래프생성
#plt.plot(graph_x,graph_y,color='blue',linestyle='-',marker='o')
if (score == None):
    score = 0

#ani = FuncAnimation(plt.gcf(), animate(), interval = 1000)

anim = FuncAnimation(fig, animate,interval=100)
#frames=200
plt.hlines(SSIM_THRESHOLD, 0, 500, color='green', linestyle='solid', linewidth=3)



plt.show()


cv2.destroyAllWindows()







 