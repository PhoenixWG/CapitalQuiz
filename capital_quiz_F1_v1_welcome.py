from tkinter import *
from tkinter import ttk

import random


class CapitalQuiz:

    def __init__(self,parent):

        self.parent = parent
        self.welcome = Frame(self.parent)
        self.welcome.pack(fill=BOTH,expand=1)

        self.title_label = Label(self.welcome, text = "Welcome to Capital Quiz",
                                bg = "black", fg = "white", font = ("Time", '14', "bold italic"))
        self.title_label.pack(side=TOP,fill=X)

              
        
if __name__ =="__main__":
    root = Tk()
    root.geometry('400x300')
    frames = CapitalQuiz(root)
    root.title("Quiz")
    root.mainloop()