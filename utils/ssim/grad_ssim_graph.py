from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import cv2
import rospy
from std_msgs.msg import Float32
import numpy as np
import time


score = None #전역변수로 선언을 해주고
FPS = 30

class graph:
    def __init__(self):
        rospy.init_node('grad_sub_node', anonymous=True)
        self.subscriber = rospy.Subscriber(
            name="GRAD", data_class=Float32, callback=self.callbackFunction)
        self.rate = rospy.Rate(30) # 0.5hz

    def callbackFunction(self,msg): #기본 argument는 구독한 메세지 객체 
        global score
        score = float(msg.data)
        print(score)
        self.rate.sleep() #100hz가 될때 까지 쉬기


g = graph()

# #그래프 정보 설정
# plt.tight_layout()
# plt.xlabel('X') #x 라벨
# plt.ylabel('Y') #y 라벨
# plt.title("TITLE") #그래프 이름

graph_x = np.array([])
graph_y = np.array([])
index = count()

# def animate():
#     global score

#     graph_x.append(next(index))
#     graph_y.append(score)
        
#     plt.cla()
#     plt.plot(graph_x, graph_y)
    
fig = plt.figure()
#ax = plt.axes(xlim=(30, 430), ylim=(0.7, 1))
ax = plt.axes(xlim=(30, 500), ylim=(0, 5))
line, = ax.plot([], [], lw=3)

x = count()

def animate(i):
  global score 
  global graph_x
  global graph_y
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
#plt.hlines(0.80, 0, 430, color='green', linestyle='solid', linewidth=3)
plt.hlines(1.0, 0, 500, color='green', linestyle='solid', linewidth=3)


time.sleep(6)
plt.show()


cv2.destroyAllWindows()







 