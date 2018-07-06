#라디오 버튼(radio button)
#라디오 버튼은 단 1개의 학목만 선택할 수있다.
from tkinter import *
root = Tk()
root.title("설문조사")
select = IntVar()
select.set(1)
language = [("Pythoin" , 1) , ("Java" , 2)  , ("C" , 3)]
def showChoice():
    print(select.get())
Label(root , text = "원하는 언어를 선택하세요 :" , justify =LEFT).pack()
#반복처리
for txt , val in language:
    Radiobutton(root , text = txt, padx=20,
                variable=select,command=showChoice,
                value=val).pack(anchor=W)
root.mainloop()