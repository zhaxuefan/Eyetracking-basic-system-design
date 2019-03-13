from tkinter import *

root = Tk()
root.title('Screen')


btnstr='123456'
btnlist=list(btnstr)

for i,text in enumerate(btnlist):
    btn=Button(root,text=text,font=25,width=40,height=11,command=lambda text=text:btnclick(text),bg='#800080',fg='#FFFFE0')
    btn.grid(row=i//3+1,column=i%3 )

root.mainloop()
