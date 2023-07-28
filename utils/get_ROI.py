import cv2
import json

FPS = 30
cap = cv2.VideoCapture("./output1.avi")
json_path = "./ROI.json"

with open(json_path, "r") as json_file:
    ROI = json.load(json_file)

# ROI = {#(x,y) (x+w,y+h)
#             #left top, right bottom
#             #x : 0 ~ 1920 (left-right), y : 0 ~ 1080 (top -bottom)
#     "book1":{'x1':100,'y1':200,'x2':1920,"y2":1780}, 
#     "book2":{'x1':100,'y1':200,'x2':1920,"y2":1780},
#     ...
#     "book9":{'x1':100,'y1':200,'x2':1920,"y2":1780}
#  }

print("width : %d, height : %d" %(cap.get(cv2.CAP_PROP_FRAME_WIDTH) , cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print("\t Press r to get RoI \n\
         Press q to Quit the terminal\
         Press s to Save the ROI")

flag= 0

while cap.isOpened():
    run,src = cap.read()
    if not run:
        print("frame is not detected")

    if cv2.waitKey(int(1000/FPS)) & 0xFF == ord('r'): #FPS 30 =>  Time  = 1000 / FPS
        book_num = int(input("Please Enter the number of Bookcase(range 1~9),[another key: Just Check]  ex) 1 : "))
        x_pos,y_pos,width,height = cv2.selectROI("VideoFrame",src,False)
        print("\n Number of bookcase : ", book_num)
        print("x position, y position : ", x_pos,"," ,y_pos)
        print("width , height : ",width,",", height)
        check = input("Do you want to save ROI ? (y/n)")
        if check == 'y':
            key = "book"+str(book_num)
            ROI[key]['x1'], ROI[key]['y1'], ROI[key]['x2'], ROI[key]['y2'] = x_pos, y_pos, x_pos+width, y_pos+height
            print("Complete to save ROI")
        else:
            print("Did not save ROI")

        flag = 1
        
    # Check the RoI
    #if flag == 1:
    #    #cv2.rectangle(frame,left top, right bottom, color(RGB), Thickness(-1:filled))
    #    cv2.rectangle(src,(x_pos,y_pos),(x_pos+width,y_pos+height), (0,0,255),-1 )
    #    #cv2.rectangle(src,ROI["book1"][0],ROI["book1"][1], (0,0,255),-1 )
    
    cv2.imshow("VideoFrame", src)
    
    if cv2.waitKey(int(1000/FPS)) & 0xFF == ord('s'): #FPS 30 =>  Time  = 1000 / FPS
        with open(json_path, 'w') as outfile:
            json.dump(ROI, outfile, indent=4)
            print("Complete to save json")
        break

    if cv2.waitKey(int(1000/FPS)) & 0xFF == ord('q'): #FPS 30 =>  Time  = 1000 / FPS
        print("Did not save the json")
        break

cv2.destroyAllWindows()