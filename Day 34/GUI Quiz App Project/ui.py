from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window =Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR, highlightthickness=0)
        
        self.score = 0
        self.finished = False
        self.score_label = Label(text=f"Score: {self.score}", font=("Ariel", 12, "normal"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(self.window, bg="white", width=300, height=250, highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, text="test", font=("Ariel", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_button)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_button)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.question_number < 10:
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button(self):
        if self.quiz.question_number <= 10 and not self.finished:
            is_true = self.quiz.check_answer("true")
            if is_true:
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
                self.canvas.configure(bg="green")
            else:
                self.canvas.configure(bg="red")
            
            if self.quiz.question_number == 10:
                self.finished = True

            self.window.after(1000, self.get_next_question)

    def false_button(self):
        if self.quiz.question_number <= 10 and not self.finished:
            is_true = self.quiz.check_answer("false")
            if is_true:
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
                self.canvas.configure(bg="green")
            else:
                self.canvas.configure(bg="red")

            if self.quiz.question_number == 10:
                self.finished = True

            self.window.after(1000, self.get_next_question)

