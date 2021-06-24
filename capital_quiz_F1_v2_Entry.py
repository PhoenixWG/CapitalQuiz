from tkinter import *
from tkinter import ttk

import random

class Question:

    def __init__(self, question, answer, dummies):
        """
            Accepts a question, the correct answer and a list of incorrect
            answers as parameters.
        """
        self.question = question
        self.answer = answer
        self.dummies = dummies
        self.set_answers()

    def set_answers(self):
        """
            Inserts the correct answer into a random position of the
            list of possible answers.
        """
        self.answers = self.dummies
        self.answers.insert(random.randrange(len(self.dummies)+1), self.answer)

class CapitalQuiz:

    def __init__(self,parent):

        self.parent = parent
        self.welcome = Frame(self.parent)
        self.welcome.pack(fill=BOTH,expand=1)

        self.title_label = Label(self.welcome, text = "Welcome to Capital Quiz",
                                bg = "black", fg = "white", font = ("Time", '14', "bold italic"))
        self.title_label.pack(side=TOP,fill=X)

        self.text_label = Label(self.welcome, text = "This quiz is intended for students aged 7-12", fg= "black", font = ("Time", '11', "italic"))
        self.text_label.pack(side=BOTTOM,fill=X)

        self.name_label = Label(self.welcome, text = "Name", anchor = W,
                               fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", '12', "bold italic"))
        self.name_label.place(x=10,y=50)

        self.age_label = Label(self.welcome, text = "Age", anchor = W,
                              fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", '12', "bold italic"))
        self.age_label.place(x=10,y=80)
        
        self.NameEntry = ttk.Entry(self.welcome, width = 20)
        self.NameEntry.place(x=90,y=60)
        
        self.AgeEntry = ttk.Entry(self.welcome, width = 20)
        self.AgeEntry.place(x=90,y=100)        
   
        
if __name__ =="__main__":
    root = Tk()
    root.geometry('400x300')
    frames = CapitalQuiz(root)
    root.title("Quiz")
    root.mainloop()