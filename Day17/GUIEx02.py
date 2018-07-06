#grid 관리자
"""
row : 행번호 지정
column : 열번호 지정
rowspan : 행의 개수 시정
columnspan : 열의 개수 지정
padx   : 위젯의 좌우 여백지정
pady  : 위젯의 상하 여백지정
sticky : 영역의 내에서 경계맞춤지정(EWSN)
"""
from tkinter import *
win = Tk()
b1 = Button(win , text = "one")
b2 = Button(win , text = "two")
b3 = Button(win , text = "three")
lb = Button(win , text = "레이블")
b1.grid(row = 0 , column = 0)
b2.grid(row = 0 , column = 1)
b3.grid(row = 0 , column = 2)
lb.grid(row = 1 , column = 0 , columnspan = 3)
win.mainloop() # 버튼 호출을 대기함

