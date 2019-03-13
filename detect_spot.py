import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image,ImageDraw

b = 1
for b in range(1, 4):
 filename = str(b) + '.jpg'
 img = Image.open(filename)
 m, n = img.size
    # print(m,n)
 img = cv2.imread(filename, 0)
 pic = img[1:n,1:int(m/2)]
    # print(pic)
 cv2.imshow('image.jpg', pic)
    # pic= img[int(m/2):m-1,1:n]
 cv2.imwrite('eye2.jpg', pic)

 img = cv2.imread('eye2.jpg', 0)

 img = cv2.medianBlur(img, 3)
 cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

 imgGray = cv2.cvtColor(cimg, cv2.COLOR_BGR2GRAY)
 #m= 158
 #for m in range(20, 100):
 #, imgOtsu = cv2.threshold(imgGray, m, 255, cv2.THRESH_BINARY)
 ret2,imgOtsu = cv2.threshold(imgGray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
 #print(ret2)
 cv2.imwrite('pic.jpg', imgOtsu)
 plt.imshow(imgOtsu, cmap='gray')

 img = cv2.imread('pic.jpg')
 #imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 #ret,binary =cv2.threshold(imgGray,0,255,cv2.THRESH_OTSU)
 ret,binary =cv2.threshold(imgGray,ret2,255,cv2.THRESH_BINARY_INV)
 image,contours, hierarchy=cv2.findContours(binary,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
#cv2.drawContours(img,contours,-1, (0, 0, 255),3)
 m=len(contours)
 #print(m)
#print(contours)
 cnt=[]
 a=cv2.contourArea(contours[0])
 for i in range(0,m):
    cnt=contours[i]
    a1=cv2.contourArea(cnt)
    if a1<=a:
        a=a1
        cntfinal=cnt
        h=i
 cv2.drawContours(img,contours,h, (0, 0, 255),2)
 cnt = contours[h]
 M = cv2.moments(cnt)
 cx = int(M['m10']/M['m00'])
 cy = int(M['m01']/M['m00'])
 print(cx,cy)
 cv2.imshow("img",img)
 cv2.waitKey(0)
 b=b+1
'''cnt=[]
a=cv2.contourArea(contours[0])
for i in range(0,m):
    cnt=contours[i]
    a1=cv2.contourArea(cnt)
    if a1<=a:
        a=a1
        cntfinal=cnt
A = cv2.minAreaRect(cntfinal)
box=cv2.boxPoints(A)
box = np.int0(box)
cv2.drawContours(img, [box], -1, (0, 0, 255), 2)'''
#cv2.drawContours(img,contours,2, (0, 0, 255))
#cv2.imshow("img",img)
#cv2.waitKey(0)