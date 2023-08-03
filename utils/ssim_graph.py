
#-*- coding:utf-8 -*-	# 한글 주석을 달기 위해 사용한다.
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
GRAD_THRESHOLD = 8
x_max = 500

'''
[Setting For SSIM Threshold]
When User input the argument for threshold
'''
if args.ST != 'DEV':
    SSIM_THRESHOLD = args.ST

if args.GT != 'DEV':
    GRAD_THRESHOLD = args.GT

print("ST = ", SSIM_THRESHOLD)
print("GT = ", GRAD_THRESHOLD)
print("mode  = ", args.mode)

g = graph()

# #그래프 정보 설정
# plt.tight_layout()
#plt.xlabel('time') #x 라벨
#plt.ylabel('Score') #y 라벨
#plt.title("SSIM") #그래프 이름


''' create the graph'''
ggraph_x = np.array([])
ggraph_y = np.array([])
sgraph_x = np.array([])
sgraph_y = np.array([])
lst = [i for i in range(x_max)]
#index = cycle(lst)

sindex = count()
gindex = count()

fig = plt.figure() #figure(도표생성)

ax1 = plt.subplot(211,xlim=(0, x_max), ylim=(0.3, 1)) #ssim
plt.title("SSIM")

ax2 = plt.subplot(212,xlim=(0, x_max), ylim=(0, 15)) #grad
plt.title("Grad")


line1, = ax1.plot([], [], lw=3)
line2, = ax2.plot([], [], lw=3)

# if args.mode == "GRAD":
#     fig = plt.figure()
#     #ax = plt.axes(xlim=(30, 430), ylim=(0.7, 1))
#     ax = plt.axes(xlim=(0, x_max), ylim=(0, 15))
#     line, = ax.plot([], [], lw=3)
# else:
#     fig = plt.figure()
#     ax = plt.axes(xlim=(0, x_max), ylim=(0.3, 1))
#     line, = ax.plot([], [], lw=3)


# def animate(i):
#     global args
#     global ssim_score
#     global graph_x
#     global graph_y
#     global state 
#     global grad
#     global index
#     if state != "open": #For only Watching graph when bookcase is opened
#         score,grad,ssim_score = 0,0,0

#     if args.mode == 'GRAD':
#         score = grad
#     elif args.mode == 'SSIM':
#         score = ssim_score
#     else:
#         print("Please Select the mode")
    
#     if next(index) >= x_max:
#         index = count()
#         graph_x,graph_y= [],[]
#         anim.frame_seq = anim.new_frame_seq()
#         anim.event_source.start()
#     else:
#         graph_x = np.append(graph_x,next(index))
#         graph_y = np.append(graph_y,score)
#     line.set_data(graph_x, graph_y)
#     return line,

def s_animate(i):
    global args
    global ssim_score
    global state 
    global sgraph_x
    global sgraph_y
    global sindex
    if state != "open": #For only Watching graph when bookcase is opened
        score,ssim_score = 0,0

    score = ssim_score
    
    if next(sindex) >= x_max:
        sindex = count()
        sgraph_x,sgraph_y= [],[]
        ssim_anim.frame_seq = ssim_anim.new_frame_seq()
        ssim_anim.event_source.start()
    else:
        sgraph_x = np.append(sgraph_x,next(sindex))
        sgraph_y = np.append(sgraph_y,score)
    line1.set_data(sgraph_x, sgraph_y)
    return line1,


def g_animate(i):
    global args
    global state 
    global grad
    global ggraph_x
    global ggraph_y
    global gindex

    if state != "open": #For only Watching graph when bookcase is opened
        score,grad = 0,0
    score = grad

    if next(gindex) >= x_max:
        gindex = count()
        ggraph_x,ggraph_y= [],[]
        grad_anim.frame_seq = grad_anim.new_frame_seq()
        grad_anim.event_source.start()
    else:
        ggraph_x = np.append(ggraph_x,next(gindex))
        ggraph_y = np.append(ggraph_y,score)
    line2.set_data(ggraph_x, ggraph_y)
    return line2,

#plt.plot(graph_x,graph_y,color='blue',linestyle='-',marker='o')
if (score == None):
    score = 0


ssim_anim = FuncAnimation(fig, s_animate,interval=100,repeat = True)
grad_anim = FuncAnimation(fig, g_animate,interval=100,repeat = True)
#frames=200


ax1.hlines(SSIM_THRESHOLD, 0, x_max, color='green', linestyle='solid', linewidth=3)
ax2.hlines(GRAD_THRESHOLD, 0, x_max, color='green', linestyle='solid', linewidth=3)
# args.mode == 'SSIM':

plt.tight_layout(h_pad=3)#, w_pad=8)
plt.show()


cv2.destroyAllWindows()







 