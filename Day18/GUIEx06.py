from tkinter import *
class App:
    def __init__(self,master):
        self.button = Button(master , text = "Quit" , fg = "red" , command =
                             master.quit)
        self.button.pack(side= LEFT)

        self.slogan = Button(master , text = "Hello" , fg = "blue" , command =
                             self.wSlogan)
        self.slogan.pack(side = LEFT)
    def wSlogan(self):
        print("Tkinter GUI")
root = Tk()
app =App(root)
root.mainloop()