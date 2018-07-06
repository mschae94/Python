
from tkinter import *
master = Tk()
var1 = IntVar()
var2 = IntVar()

def state():
    print("프로그래머: %d\n디자이너:%d"%(var1.get() , var2.get()))
Label(master , text = "직업선택:").grid(row =0 , sticky = W)

var1 = IntVar()
Checkbutton(master, text= "프로그래머" , variable = var1).grid(row =1,sticky =W)
var2 = IntVar()
Checkbutton(master, text = "디자이너" , variable = var2).grid(row = 2, sticky =W)
b1 = Button(master , text = "작업마침" , command=master.quit)
b1.grid(row =3 , sticky = W , pady = 4)
b2 = Button(master , text= "결과출력" , command = state)
b2.grid(row = 4 , sticky = W , pady = 4)
master.mainloop()
