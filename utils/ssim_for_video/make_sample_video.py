import datetime
import cv2

capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
record = False

while True:


    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

    now = datetime.datetime.now().strftime("%d_%H-%M-%S")

    #27 = ESC, 26 = Ctrl + Z, 24 = Ctrl + X, 3 = Ctrl + C

    if cv2.waitKey(1) & 0xFF == ord('r'):
        print("녹화 시작")
        record = True
        video = cv2.VideoWriter("./" + str(now) + ".avi", fourcc, 20.0, (frame.shape[1], frame.shape[0]))

    elif cv2.waitKey(1) & 0xFF == ord('x'):
        print("녹화 중지")
        record = False
        video.release()
        break
        
    if record == True:
        print("녹화 중..")
        video.write(frame)

capture.release()
cv2.destroyAllWindows()