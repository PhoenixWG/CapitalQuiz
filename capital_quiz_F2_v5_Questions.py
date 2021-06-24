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
        
        #Drop down for Age
        tkvar = IntVar(root)
        
        age_range = [7, 8, 9, 10, 11, 12]
        tkvar.set(7)
        
        self.age_drop_down = OptionMenu(self.welcome, tkvar, *age_range)
        self.age_drop_down.place(x=120,y=90)
        self.age_drop_down.config(width=20)
                            
        
        self.name_entry = ttk.Entry(self.welcome, width = 20)
        self.name_entry.place(x=120,y=55)
                         
        self.next_button = ttk.Button(self.welcome, text = 'Questions', command = self.show_questions)
        self.next_button.place(x=80,y=150)
        
        self.questions = Frame(self.parent)
        
        self.questions_label = Label(self.questions, text = "Questions",
                                    bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                                    font = ("Time", '14', "bold italic"))
        self.once_done=False
        self.questions_label.pack(side=TOP,fill=X,anchor="w")
        
        Label(self.questions, text = "Q1.  What is the capital of United States?",font=("arial",12,"bold")).place(x=10,y=50)
        self.capital_one=StringVar()
        self.capital_one.set("hellow")
        Radiobutton(self.questions,text="Washington DC",font=("arial",12),variable=self.capital_one,value="Washington DC").place(x=20,y=80)
        Radiobutton(self.questions,text="London",font=("arial",12),variable=self.capital_one,value="London").place(x=20,y=110)
        Radiobutton(self.questions,text="Delhi",font=("arial",12),variable=self.capital_one,value="Delhi").place(x=20,y=140)
        Radiobutton(self.questions,text="Tokyo",font=("arial",12),variable=self.capital_one,value="Tokyo").place(x=20,y=170)
        Label(self.questions, text = "Q2.  What is the capital of Australia?",font=("arial",12,"bold")).place(x=10,y=200)
        self.capital_two=StringVar()
        self.capital_two.set("hellow")
        Radiobutton(self.questions,text="Canberra",font=("arial",12),variable=self.capital_two,value="Canberra").place(x=20,y=230)
        Radiobutton(self.questions,text="Islamabad",font=("arial",12),variable=self.capital_two,value="Islamabad").place(x=20,y=260)
        Radiobutton(self.questions,text="Delhi",font=("arial",12),variable=self.capital_two,value="Delhi").place(x=20,y=290)
        Radiobutton(self.questions,text="Tokyo",font=("arial",12),variable=self.capital_two,value="Tokyo").place(x=20,y=320)
        Label(self.questions, text = "Q3.  Tokyo is the capital of which country?",font=("arial",12,"bold")).place(x=10,y=350)
        self.capital_three=StringVar()
        self.capital_three.set("hellow")
        Radiobutton(self.questions,text="Japan",font=("arial",12),variable=self.capital_three,value="Japan").place(x=20,y=380)
        Radiobutton(self.questions,text="Canada",font=("arial",12),variable=self.capital_three,value="Canada").place(x=20,y=410)
        Radiobutton(self.questions,text="India",font=("arial",12),variable=self.capital_three,value="India").place(x=20,y=440)
        Radiobutton(self.questions,text="Spain",font=("arial",12),variable=self.capital_three,value="Spain").place(x=20,y=470)
        Label(self.questions, text = "Q4.  What is the capital of Taiwan?",font=("arial",12,"bold")).place(x=10,y=500)
        self.capital_four=StringVar()
        self.capital_four.set("hellow")
        Radiobutton(self.questions,text="Taipei",font=("arial",12),variable=self.capital_four,value="Taipei").place(x=20,y=530)
        Radiobutton(self.questions,text="Paris",font=("arial",12),variable=self.capital_four,value="Paris").place(x=20,y=560)
        Radiobutton(self.questions,text="Madrid",font=("arial",12),variable=self.capital_four,value="Madrid").place(x=20,y=590)
        Radiobutton(self.questions,text="Beijing",font=("arial",12),variable=self.capital_four,value="Beijing").place(x=20,y=620)
        Label(self.questions, text = "Q5.  State True or False: Beijing is the capital of China?",font=("arial",12,"bold")).place(x=10,y=650)
        self.capital_five=StringVar()
        self.capital_five.set("hellow")
        Radiobutton(self.questions,text="True",font=("arial",12),variable=self.capital_five,value="True").place(x=20,y=680)
        Radiobutton(self.questions,text="False",font=("arial",12),variable=self.capital_five,value="False").place(x=20,y=710)
        self.home_button = ttk.Button(self.questions, text = 'Home', command = self.show_welcome)
        self.home_button.place(x=30,y=760)
        self.submit_button = ttk.Button(self.questions, text = 'Submit', command = self.submit)
        self.submit_button.place(x=130,y=760)
        
            
    def submit(self):
        count=0
        if self.capital_one.get()=="Washington DC":
            count+=1
        if self.capital_two.get()=="Canberra":
            count+=1
        if self.capital_three.get()=="Japan":
            count+=1
        if self.capital_four.get()=="Taipei":
            count+=1
        if self.capital_five.get()=="True":
            count+=1
        Label(self.questions,font=("arial",40,"bold"),text=f"You scored: {str(count)}/5").place(x=500,y=50)
        self.c=count
        self.capital_five.set("hellow")
        self.capital_four.set("hellow")
        self.capital_three.set("hellow")
        self.capital_two.set("hellow")
        self.capital_one.set("hellow")
        self.once_done=True
        self.submit_button.config(state=DISABLED)
        
    def show_welcome(self):
        if self.once_done==True:
            for i in self.questions.winfo_children():
                i.destroy()
            self.questions.pack_forget()
        else:
            self.questions.pack_forget()
        self.welcome.pack(fill=BOTH,expand=1)
                
                             
    def show_questions(self):
        self.welcome.pack_forget()
        if self.once_done==True:
            self.questions.pack(fill=BOTH,expand=1)
            Label(self.questions,font=("arial",40,"bold"),text=f"You scored: {str(self.c)}/5").place(x=500,y=50)
            Label(self.questions,font=("arial",30,"bold"),text="You can only attempt the quiz once.").place(x=500,y=160)
        else:
            self.questions.pack(fill=BOTH,expand=1)

if __name__ =="__main__":
    root = Tk()
    root.geometry('400x300')
    frames = CapitalQuiz(root)
    root. title("Quiz")
    root . mainloop()