from tkinter import *
root = Tk()
def wSlogan():
    print("Tkinter GUI")
button = Button(root , text = "Quit" , fg = "red" , command = root.quit)
button.pack(side = LEFT)
slogan = Button(root , text = "Hello" , fg= "blue" , command = wSlogan)
slogan.pack(side = LEFT)
root.mainloop()