#엔트리(Etry)

"""
엔트리위젯은 1줄짜리의 간단한 텍스트 항목을 입력받을때 주로 사용된다.
"""

from tkinter import*
master =Tk()
master.title("항목입력")

Label(master , text = "아이디").grid(row= 0)
Label(master , text = "비밀번호").grid(row = 1)
e1 = Entry(master)
e2 = Entry(master)

e1.grid(row = 0 , column = 1)
e2.grid(row = 1 , column = 1)

master.mainloop()
