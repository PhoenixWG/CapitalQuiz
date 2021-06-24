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

        #Drop down for Age
        tkvar = IntVar(root)

        age_range = [7, 8, 9, 10, 11, 12]
        tkvar.set(7)

        self.age_drop_down = OptionMenu(self.welcome, tkvar, *age_range)
        self.age_drop_down.place(x=120,y=90)
        self.age_drop_down.config(width=20)
        
        self.warning_label = Label(self.welcome, text = "", anchor=W,
                                   fg = "red", width = 20, padx = 30, pady = 10)
        self.warning_label.place(x=140,y=120)

        self.name_entry = ttk.Entry(self.welcome, width = 20)
        self.name_entry.place(x=120,y=55)

        self.next_button = ttk.Button(self.welcome, text = 'Questions', command = self.question)
        self.next_button.place(x=80,y=150)
        
    def question(self):
        try:
            if self.name_entry.get() == "":
                self.warning_label.configure(text = "Please enter name")
                self.name_entry.focus()
                
            elif self.name_entry.get().isalpha() == False:
                self.warning_label.configure(text = "Please enter text")
                self.name_entry.delete(0, END)
                self.name_entry.focus()
                
            else:
                self.welcome.destroy()
                c = Quiz(self.parent)
                c.next_question()
        
        except ValueError:
            self.warning_label.configure(text = "Please enter a proper name")
            self.name_entry.delete(0, END)
            self.name_entry.focus()
            
    
class Quiz:

    def __init__(self, parent):
        """
            Sets up the GUI, including ensuring space is preserved for the
            message to the user to be displayed.The number of choices provided
            for each question is assumed to be the same.
        """
        self.parent = parent
        self.index = 0 # for keeping track of which question we are up to
        self.correct = 0 # for keeping track of hjow many the user has got correct
        #formatting constants
        PX = 10
        PY = 10
        PY_RADIO = 3

        # Creates a list of Question objects
        self.questions = []
        q_file = open("questions.txt")
        q_list = q_file.readlines()
        for line in q_list:
            line = line[:-1] # removing newline character from the end
            tokens = line.split(",")
            self.questions.append(Question(tokens[0], tokens[1], tokens[2:]))
            
        self.Frame3 = Frame(parent)
        self.Frame3.pack(fill=BOTH,expand=1)

        #Sets up the GUI
        self.question_section_label = Label(self.Frame3, text = "Question:", anchor = NW, width = 10, pady = PY, padx = PX)
        self.question_section_label.grid(row = 0, column = 0, sticky = NW)

        self.question_label = Label(self.Frame3, text = "",  anchor = NW, pady = PY, padx = PX, wraplength = 220, height = 2, width = 40)
        self.question_label.grid(row = 0, column = 1, sticky = NW)

        self.question_label.configure(text = self.questions[self.index].question)

        #Creates variable for Radiobuttons and sets it to zero so that
        #no options are shown as selected
        self.var = StringVar()
        self.var.set(0)

        # Radiobuttons are now stored in a list so that they may be easily
        # reconfigured for the next question. The number of choices provided
        # for each question is assumed to be the same
        self.rbs = []
        self.num_choices = len(self.questions[self.index].answers)
        for i in range(self.num_choices):
            ans_txt = self.questions[self.index].answers[i]
            self.rbs.append(Radiobutton(self.Frame3, text = ans_txt, variable = self.var, value = ans_txt, command = self.process_question, pady = 3))
            self.rbs[i].grid(row = i+1, column = 1,  sticky = NW)

        self.feedback = Label(self.Frame3, text = "", height = 3, font = ("Times", "12", "bold"), wraplength = 200)
        self.feedback.grid(row = self.num_choices + 1,  columnspan = 2)

        self.finish_btn = Button(self.Frame3, text = "Finish", width = 4, command = self.finish_quiz)
        self.finish_btn.grid(row = self.num_choices + 2, column = 0, sticky = W, padx = PX, pady = PY)

        self.next_btn = Button(self.Frame3, text = "Next", width = 4, command = self.next_question)
        self.next_btn.grid(row = self.num_choices + 2, column = 1, sticky = E, padx = PX, pady = PY)

    def process_question(self):
        """
            Disables the RadioButtons. Checks if the selected answer is the correct one and provides appropriate feedback
        """
        for rb in self.rbs:
            rb.configure(state = DISABLED)
        if self.var.get()==self.questions[self.index].answer:
            self.correct += 1
            self.feedback.config(text = "Correct!  " + str(self.correct) + "/" + str(self.index))
        else:
            self.feedback.config(text = "Incorrect! The answer is "+ self.questions[self.index].answer + "  " +
                                 str(self.correct) + "/" + str(self.index + 1))

    def next_question(self):
        """
            If the end of the question list has not been reached, the index is incremented and
            the question Label and Radiobuttons are reconfigured with the appropriate text from
            the next Question object.
        """
        # There is still another question to ask
        if self.index < len(self.questions) - 1:
            for rb in self.rbs:
                rb.configure(state = NORMAL)
            self.index+=1
            self.question_label.configure(text = self.questions[self.index].question)

            self.var = StringVar()
            self.var.set(0)
            for i in range(len(self.questions[self.index].answers)):
                ans_txt = self.questions[self.index].answers[i]
                self.rbs[i].configure(text = ans_txt, variable = self.var, value = ans_txt )
            self.feedback.config(text = "", height = 3)
        else:
            self.finish_quiz()

    def finish_quiz(self):
        """ The question Labels and Radionbuttons are removed and the feedback label
            is reconfigured to display a message informing the user that the quiz is
            over and the number they got correct. The height of the feedback Label is
            also reconfigured to stop the window resizing too dramatically."""
        self.question_section_label.configure(text = "")
        self.question_label.configure(text = "")
        for rb in self.rbs:
            rb.grid_remove()
        self.feedback.config(text = "Quiz over. You got " + str(self.correct) + " out of " + str(self.index),
                              height = 10)
        self.next_btn.grid_remove()
        self.finish_btn.configure( width = 15, command = self.resume_quiz)
        if self.index + 1 == len(self.questions):
            self.finish_btn.configure(text = "Retake Quiz")
        else:
            self.finish_btn.configure(text = "Resume Quiz")

    def resume_quiz(self):
        """ Presents either the next question from where they were up to (resume) or question 1(retake)"""
        if self.index + 1== len(self.questions):
            self.correct = 0
            self.index = -1
        for rb in self.rbs:
            rb.grid()
        # replacing a few bits not covered in self.next_question
        self.question_section_label.configure(text = "")
        self.finish_btn.configure(text = "Finish", width = 10, command = self.finish_quiz)
        self.next_btn.grid()
        # Presents either the next question from where they were up to or question 1
        self.next_question()  
           
        
if __name__ =="__main__":
    root = Tk()
    root.geometry('400x300')
    frames = CapitalQuiz(root)
    root.title("Quiz")
    root.mainloop()