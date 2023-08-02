import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count,cycle
import cv2
import rospy
from std_msgs.msg import Float32,String
import numpy as np
import time
import argparse

parser = argparse.ArgumentParser(description='Program for Graph (mode : SSIM/GRAD)')
parser.add_argument('--mode',help= "Select GRAD or SSIM(default = 'GRAD')",default = 'GRAD')

parser.add_argument('--ST',help= "SSIM Threshold(default = developer setting)",default = 'DEV')
parser.add_argument('--GT',help= "GRAD Threshold(default = developer setting))",default = 'DEV')

args = parser.parse_args() #


score = None
ssim_score = None #Using For Global
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
        global ssim_score
        ssim_score = float(msg.data)
        self.rate.sleep() #100hz가 될때 까지 쉬기

    def callbackFunction2(self,msg): #기본 argument는 구독한 메세지 객체 
        global state
        state = msg.data
        self.rate.sleep() #100hz가 될때 까지 쉬기

    def callbackFunction3(self,msg): #기본 argument는 구독한 메세지 객체 
        global grad
        grad = float(msg.data)
        self.rate.sleep() #100hz가 될때 까지 쉬기





SSIM_THRESHOLD = 0.65
GRAD_THRESHOLD = 0.65
x_max = 500

'''
[Setting For SSIM Threshold]
When User input the argument for threshold
'''
if args.ST != 'DEV':
    SSIM_THRESHOLD = args.ST

if args.GT != 'DEV':
    GRAD_THRESHOLD = args.GT

g = graph()

# #그래프 정보 설정
# plt.tight_layout()
#plt.xlabel('time') #x 라벨
#plt.ylabel('Score') #y 라벨
#plt.title("SSIM") #그래프 이름


''' create the graph'''
graph_x = np.array([])
graph_y = np.array([])



fig = plt.figure()
ax = plt.axes(xlim=(30, x_max), ylim=(0.3, 1))
line, = ax.plot([], [], lw=3)

def animate(index,mode):
    global ssim_score
    global graph_x
    global graph_y
    global state 
    global grad
    if state != "open": #For only Watching graph when bookcase is opened
        score,grad,ssim_score = 0,0,0
    if mode == 'GRAD':
        score = grad
    elif mode == 'SSIM':
        score = ssim_score
    else:
        print("Please Select the mode")
    graph_x = np.append(graph_x,next(index))
    graph_y = np.append(graph_y,score)
    line.set_data(graph_x, graph_y)
    return line,


#plt.plot(graph_x,graph_y,color='blue',linestyle='-',marker='o')
if (score == None):
    score = 0


lst = [i for i in range(x_max)]
index = cycle(lst)
anim = FuncAnimation(fig, animate(index,args.mode),interval=100)
#frames=200
plt.hlines(SSIM_THRESHOLD, 0, x_max, color='green', linestyle='solid', linewidth=3)



plt.show()


cv2.destroyAllWindows()







 