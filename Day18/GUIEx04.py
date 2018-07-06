

#이벤트: 위젯을 클릭했을 때 특정 작업을 실행시키는것!
"""
StringVar() :문자열
InVar() : 정수
DoubleVar() :실수
BoolleanVar() : 논리값 (참 , 거짓)
"""
from tkinter import *
win = Tk()
t = StringVar()
def Func1():
    t.set("1") # set 저장 , 쓰기
    print("현재 클릭된 버튼: ", t.get() # get 가져오기 , 읽기
          )
def Func2():
    t.set("2")
    print("현재 클릭된 버튼: " , t.get())
b1 = Button(win ,text = "one", command = Func1) #이름만적자

#색상 과 폰트
b1["fg"] = "red" #글자색
b1["bg"] = "yellow" #버튼배경색
b1["font"] = "Times" , 10 , "bold" # 버튼서체


b1.pack(side = LEFT , fill =X , padx =110 , pady = 10 , expand = YES)
b2 = Button(win , text = "two" , command = Func2)
b2.pack(side = RIGHT , fill = X , padx = 10 , pady = 100 , expand = YES)
win.mainloop()
