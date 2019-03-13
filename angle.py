

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 20:40:25 2014
@author: duan
"""
import numpy as np
import cv2
from PIL import Image,ImageDraw
from matplotlib import pyplot as plt
#import skimage.io as io
#from skimage import data_dir

#data_dir='C:/Users/Administrator/PycharmProjects/untitled10'
#str=data_dir + '/*.jpg'
#coll = io.ImageCollection(str)
s=2
for s in range(2,3):
 filename=str(s)+'.jpg'
 img=Image.open(filename)
 m,n=img.size
#print(m,n)
 m1=m/2
 print(m,n)
 #print(int(m/2))
 img = cv2.imread(filename)
 a=np.shape(img)
 print(a)

 gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
# 返回的结果是[[ 311., 250.]] 两层括号的数组。
 corners = np.int0(corners)
 num=[]
 for i in corners:
    x,y= i.ravel()
    num.append(x-m1)

#num=np.abs(num)
 num=sorted(num)
 num2=[]
 num3=[]
 for i in range (len(num)):
    if num[i]>0:
        num2.append(num[i])
    else:
        num3.append(num[i])

 big=num2[0]
 '''if big<20:
  big=num2[1]
  if big<20:
      big=num2[2]
      if big<20:
          big=num2[3]
 else:
    big=num2[0]
'''
 num3=sorted(np.abs(num3))
 small=(num3[0])
 '''if small<20:
  small=num3[1]
  if small<20:
      small=num3[2]
      if small<20:
          small=num3[3]
 else:
    small=num3[0]
'''

 for i in corners:
    x,y= i.ravel()
    diff=x-m1
    if diff == big:
        cv2.circle(img,(x,y),3,255,-1)
        label_x=x
        label_y=y
    elif np.abs(diff) == small:
        cv2.circle(img,(x,y),3,255,-1)
        label2_x=x
        label2_y=y
 #plt.imshow(img),plt.show()


 #print(label2_x)
 #print(label2_y)
 print(label_x-int(m/2))
 print(label_y)
 print(s)
 plt.imshow(img), plt.show()
 s=s+1





















