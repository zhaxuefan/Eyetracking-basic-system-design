def face_eye():
    import numpy as np
    import cv2
    from matplotlib import pyplot as plt 
    c=1  
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

    if cap.isOpened(): #判断是否正常打开  
        rval , img = cap.read()  
    else:  
        rval = False
  
    timeF = 10  #视频帧计数间隔频率

    face_cascade = cv2.CascadeClassifier('F:/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
    #eye_cascade = cv2.CascadeClassifier('D:/Anacond  a3/opencv/sources/data/haarcascades/haarcascade_eye.xml')
 
    while rval:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.rectangle(img,(x+int(1/6*w),y+int(2/7*h)),(x+int(5/6*w),y+int(1/2*h)),(0,0,255),2)
            pic=img[y+int(2/7*h):y+int(1/2*h),x+int(1/6*w):x+int(5/6*w)]
  
            if(c%timeF == 0):
            #每隔timeF帧进行存储操作  
                #cv2.imwrite('E:/image/'+str(c) + '.jpg',img) #存储为图像
                cv2.imwrite('E:/eyes/mm/'+str(int(c/10)) + '.jpg',pic)
            c = c + 1   
        cv2.imshow('img',img)
        if cv2.waitKey(30) & 0xFF == ord('m'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
 
face_eye()