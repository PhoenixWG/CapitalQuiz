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
        
        self.text_label = Label(self.welcome, text = "This quiz is intended for students aged 7-12", fg= "black", font = ("Time", '11', "italic"))
        self.text_label.pack(side=BOTTOM,fill=X)
        
        self.name_label = Label(self.welcome, text = "Name", anchor = W, 
                               fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", '12', "bold italic"))
        self.name_label.place(x=10,y=50)
        
        self.age_label = Label(self.welcome, text = "Age", anchor = W, 
                              fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", '12', "bold italic"))
        self.age_label.place(x=10,y=80)
        
        self.age_entry = ttk.Entry(self.welcome, width = 20)
        self.age_entry.place(x=120,y=90)
                            
        
        self.name_entry = ttk.Entry(self.welcome, width = 20)
        self.name_entry.place(x=120,y=55)
                         
        self.next_button = ttk.Button(self.welcome, text = 'Questions')
        self.next_button.place(x=80,y=150)
    

if __name__ =="__main__":
    root = Tk()
    root.geometry('400x300')
    frames = CapitalQuiz(root)
    root. title("Quiz")
    root . mainloop()