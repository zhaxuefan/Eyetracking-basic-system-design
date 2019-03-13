#coding: utf-8
import scipy
from keras.models import model_from_json
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
from tkinter import *
from tkinter.ttk import *
root=Tk()
root.title('calculator')
root.geometry('250x150')
root.resizable(width=True,height=True)
var=StringVar()
display=Entry(root,textvariable=var)
display.grid(row=0, column=0, columnspan=4)

bt1=Button(root,text='1',width=10).grid(row=1,column=0)
bt2=Button(root,text='2',width=10).grid(row=1,column=1)
bt3=Button(root,text='+',width=10).grid(row=1,column=2)
bt4=Button(root,text='3',width=10).grid(row=2,column=0)
bt5=Button(root,text='4',width=10).grid(row=2,column=1)
bt6=Button(root,text='-',width=10).grid(row=2,column=2)
bt7=Button(root,text='=',width=10).grid(row=3,column=0)
bt8=Button(root,text='C',width=10).grid(row=3,column=1)
bt9=Button(root,text='*',width=10).grid(row=3,column=2)




def btclick(x):
    if x==1:
      var.set(var.get()+'1')
    elif x==2:
      var.set(display.get()+'2')
    elif x == 3:
      var.set(display.get()+'+')
    elif x == 4:
      var.set(display.get()+'3')
    elif x==5:
      var.set(display.get()+'4')
    elif x==6:
      var.set(display.get()+'-')
    elif x==7:
        if '+' in display.get():
            ret = display.get().split('+')
            var.set(float(ret[0]) + float(ret[1]))
        if '-' in display.get():
            ret = display.get().split('-')
            var.set(float(ret[0]) - float(ret[1]))
        if '*' in display.get():
            ret = display.get().split('*')
            var.set(float(ret[0]) * float(ret[1]))
        if '/' in display.get():
            ret = display.get().split('/')
            var.set(float(ret[0]) / float(ret[1]))
    elif x ==8:
       var.set('')
    elif x == 9:
      var.set(display.get() + '*')
#display.grid(row=0,column=0,columnspan=4)
#root.mainloop()
m=1
numb=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
timeF = 1
consti=True
while consti:
    if (m % timeF == 0):
       lena = mpimg.imread('E:/eyes/num/'+str(m) +'.jpg') # 读取和代码处于同一目录下的
       lena=scipy.misc.imresize(lena,(150,150,3))
 #plt.show()  # 显示图片
       lena = lena.reshape(-1, 150, 150, 3).astype('float32')
       lena = lena/255    #统一格式
       model = model_from_json(open('model9class.json').read())
       model.load_weights('first_try9class.h5')    #加载模型
       pre=int(model.predict_classes(lena)+1)   #  预测
       numb[int(m)]=btclick(pre)
       print(var.get())
       #display = Entry(root, textvariable=var)
       #display.grid(row=0, column=0, columnspan=4)
       #root.mainloop()
    if (m ==8):
        consti=False
    m=m+1
root.mainloop()