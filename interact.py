import cv2  
import numpy as np
import matplotlib.pyplot as plot
from PIL import Image,ImageDraw


cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
m,n=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
m1=m/2
fourcc = cv2.VideoWriter_fourcc('I','4','2','0')
video = cv2.VideoWriter("3.avi", fourcc, 5, size)

face_cascade =cv2.CascadeClassifier("E:/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml")

while(1):
    # get a frame
    ret, img = cap.read()
    faces = face_cascade.detectMultiScale(img, 1.2, 2, cv2.CASCADE_SCALE_IMAGE,(20,20))
    if len(faces)>0:  
        for faceRect in faces:   
                x, y, w, h = faceRect  
                cv2.rectangle(img, (int(x), int(y)), (int(x)+int(w), int(y)+int(h)), (0,255,0),2,0)
                eyes=cv2.rectangle(img,(int(x+1/6*w),int(y+2/7*h)),(int(x+5/6*w),int(y+1/2*h)),(255,0,0),2,0)
                img1=img[x:int(x+5/6*w),y:int(y+1/2*h)]
                cv2.imshow(img1)
                gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
                corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
                # 返回的结果是[[ 311., 250.]] 两层括号的数组。
                corners = np.int0(corners)
                num = []
                for i in corners:
                    x, y = i.ravel()
                    num.append(x - m1)

                # num=np.abs(num)
                num = sorted(num)
                num2 = []
                num3 = []
                for i in range(len(num)):
                    if num[i] > 0:
                        num2.append(num[i])
                    else:
                        num3.append(num[i])

                big = num2[0]
                num3 = sorted(np.abs(num3))
                small = (num3[0])

                for i in corners:
                    x, y = i.ravel()
                    diff = x - m1
                    if diff == big:
                        cv2.circle(img1, (x, y), 3, 255, -1)
                        label_x = x
                        label_y = y
                    elif np.abs(diff) == small:
                        cv2.circle(img1, (x, y), 3, 255, -1)
                        label2_x = x
                        label2_y = y
                cv2.rectangle(img1, (label_x - 10, label_y - int(1 / 3 * n)),
                              (label_x - 10 + int(1 / 3 * m), label_y + int(1 / 6 * n)), (0, 255, 0), 1)
                cv2.rectangle(img1, (label2_x + 10, label2_y - int(1 / 3 * n)),
                              (label2_x + 10 - int(1 / 3 * m), label2_y + int(1 / 6 * n)), (0, 255, 0), 1)
    video.write(img)  
    #video.write(img)  
    cv2.imshow('video',img)
    key=cv2.waitKey(1)  
    if key==ord('m'):
        break  
    # show a frame
    cv2.imshow("capture", img)
    if cv2.waitKey(1) & 0xFF == ord('m'):
        break



cap.release()
cv2.destroyAllWindows() 
