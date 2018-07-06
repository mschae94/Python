
#추석 숙제!!!! 버튼들을이용해서 사칙연산 계산기
from tkinter import *
win = Tk()
b1 = Button(win , text= "One")
b2 = Button(win , text= "Two")
b3 = Button(win , text = "Three")
b1.grid(row = 0 , column = 0)
b2.grid(row = 0 , column = 1)
b3.grid(row = 1 , column = 0)

win.mainloop()
