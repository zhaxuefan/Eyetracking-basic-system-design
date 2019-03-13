from tkinter import *
root=Tk()
root.title('calculator')
root.geometry('200x100')
root.resizable(width=True,height=True)

def bt1click():
    var.set(var.get()+'1')
def bt2click():
    var.set(display.get()+'2')
def bt3click():
    var.set(display.get()+'3')
def bt4click():
    var.set(display.get()+'4')
def bt5click():
    var.set(display.get()+'5')
def bt6click():
    var.set(display.get()+'6')
def bt7click():
    var.set(display.get()+'7')
def bt8click():
    var.set(display.get()+'8')
def bt9click():
    var.set(display.get()+'9')
def bt0click():
    var.set(display.get()+'0')
def bt_addclick():
    var.set(display.get()+'+')
def bt_subclick():
    var.set(display.get()+'-')
def bt_mulclick():
    var.set(display.get()+'*')
def bt_divclick():
    var.set(display.get()+'/')
def bt_clearclick():
    var.set('')
def bt_pointclick():
    var.set(display.get()+'.')
def calc(): 
    '''try: 
        display.set(eval(display.get())) 
    except: 
        display.set("ERROR")'''
    if '+' in display.get():

        ret=display.get().split('+')
        var.set(float(ret[0])+float(ret[1]))
    if '-' in display.get():
        ret=display.get().split('-')
        var.set(float(ret[0])-float(ret[1]))
    if '*' in display.get():
        ret=display.get().split('*')
        var.set(float(ret[0])*float(ret[1]))
    if '/' in display.get():
        ret=display.get().split('/')
        var.set(float(ret[0])/float(ret[1]))
var=StringVar()   
display=Entry(root,textvariable=var)
display.grid(row=0,column=0,columnspan=4)


'''bt1=Button(root,text='1',command=bt1click,width=10).grid(row=1,column=0)
bt2=Button(root,text='2',command=bt2click,width=10).grid(row=1,column=1)
bt3=Button(root,text='3',command=bt3click,width=10).grid(row=1,column=2)
bt4=Button(root,text='4',command=bt4click,width=10).grid(row=2,column=0)
bt5=Button(root,text='5',command=bt5click,width=10).grid(row=2,column=1)
bt6=Button(root,text='6',command=bt6click,width=10).grid(row=2,column=2)
bt7=Button(root,text='7',command=bt7click,width=10).grid(row=3,column=0)
bt8=Button(root,text='8',command=bt8click,width=10).grid(row=3,column=1)
bt9=Button(root,text='9',command=bt9click,width=10).grid(row=3,column=2)
bt0=Button(root,text='0',command=bt0click,width=10).grid(row=4,column=1)
bt_add=Button(root,text='+',command=bt_addclick,width=10).grid(row=1,column=3)
bt_sub=Button(root,text='-',command=bt_subclick,width=10).grid(row=2,column=3)
bt_mul=Button(root,text='*',command=bt_mulclick,width=10).grid(row=3,column=3)
bt_div=Button(root,text='/',command=bt_divclick,width=10).grid(row=4,column=3)
bt_clear=Button(root,text='C',command=bt_clearclick,width=10).grid(row=4,column=2)
bt_point=Button(root,text='.',command=bt_pointclick,width=10).grid(row=4,column=0)
bt_equal=Button(root,text='=',command=calc,width=10).grid(row=5,column=1,columnspan=2)'''
