import scipy
import cv2
import numpy as np
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
from tkinter import *
def formx(x,y):
    p1=294
    p2=-258
    p3=15
    p4=10
    p5=186
    p6=4
    p7=1
    p8=-182
    z2 = p1 +p2 / (1 + ((x - p3) / p4) **2) + p5 / (1 + ((y - p6) / p7) **2)+ p8 / ((1 + ((x - p3) / p4) **2) * (1 + ((y - p6) / p7) **2))
    return z2
def formy(x,y):
    p1=95.8942968393279
    p2=- 5.30821334281027
    p3=0.263532545737795
    p4= - 0.00395848879742182
    p5=- 108.61671841535
    p6=48.4369365028422
    p7=- 0.0222827713286555
    p8=0.00079666634217376
    p9=- 0.340936042442846
    p10= - 1.71444583373685
    p11=1.28936598814728
    p12=0.517025020688351
    z1 = (p1 + p2 * x + p3 * x** 2 + p4 * x **3 + p5 * p12 * np.log(y) + p6 * (p12 * np.log(y))**2) / (1 + p7 * x + p8 * x**2 + p9 * p12 * np.log(y) + p10 * (p12 * np.log(y))** 2 + p11 * (p12 * np.log(y)) **3)
    return z1

def screen(x,y):
    if x>=0 and x<=78:
        if y>=0 and y<=20:
            z=1
        elif y>20 and y<=40:
            z=4
        elif y>40 and y<=60:
            z=7
    elif x >78 and x <= 156:
        if y >= 0 and y <= 20:
            z = 2
        elif y > 20 and y <= 40:
            z = 5
        elif y > 40 and y <= 60:
            z = 8
    elif x >156 and x <= 234:
        if y >= 0 and y <= 20:
            z = 3
        elif y > 20 and y <= 40:
            z = 6
        elif y > 40 and y <= 60:
            z = 9
    return z

root=Tk()
root.title('calculator')
root.geometry('200x100')
root.resizable(width=True,height=True)
def btclick(x):
    if x==1:
      var.set(var.get()+'1')
    elif x==9:
      var.set(display.get()+'2')
    elif x == 3:
      var.set(display.get()+'3')
    elif x == 4:
      var.set(display.get()+'4')
    elif x==5:
      var.set(display.get()+'5')
    elif x==6:
      var.set(display.get()+'6')
    elif x==7:
      var.set(display.get()+'+')
    elif x ==8:
      var.set(display.get()+'-')
    elif x == 2:

       if '+' in display.get():
         ret=display.get().split('+')
         var.set(float(ret[0])+float(ret[1]))
       if '-' in display.get():
         ret=display.get().split('-')
         var.set(float(ret[0])-float(ret[1]))
var=StringVar()
display=Entry(root,textvariable=var)

c=1
numb=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
timeF =10
consti=True
while consti:
    if (c % timeF == 0):
        filename = 'E:/eyes/'+str(c) + '.jpg'
        img_first = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
        opp = np.shape(img_first)
        m=opp[1]
        n=opp[0]
        img = img_first[1:n,1:int(m/2)]
        img = cv2.medianBlur(img, 5)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        loop = 10
        for loop in range(10, 150):
            threshold, img = cv2.threshold(imgGray, loop, 255, cv2.THRESH_BINARY)
            img = cv2.medianBlur(img, 5)
            cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=5, param2=15, minRadius=0, maxRadius=0)
            if circles is None:
                loop = loop + 1
                continue
            else:
                break

        if circles is None:
            print('no')
        else:
            circles = np.uint16(np.around(circles))
            for j in circles[0, :]:
                cv2.circle(cimg, (j[0],j[1]), j[2], (0, 255, 0), 2)
                cv2.circle(cimg, (j[0], j[1]), 2, (0, 0, 255), 3)




        img_second = cv2.imread(filename)
        gray = cv2.cvtColor(img_second, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
        # 返回的结果是[[ 311., 250.]] 两层括号的数组。
        corners = np.int0(corners)
        num = []
        for i in corners:
            x, y = i.ravel()
            num.append(x - (m / 2))

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
            diff = x - (m / 2)
            if diff == big:
                cv2.circle(img, (x, y), 3, 255, -1)
                label_x = x
                label_y = y
            elif np.abs(diff) == small:
                cv2.circle(img, (x, y), 3, 255, -1)
                label2_x = x
                label2_y = y
        gapx=label2_x-j[0]
        gapy=label2_y-j[1]
        prex=formx(gapx,gapy)
        prey=formy(gapx,gapy)
        pre=screen(prex,prey)
        display.grid(row=0, column=0, columnspan=4)
    if (c ==100):
        consti=False
    c=c+1
root.mainloop()





