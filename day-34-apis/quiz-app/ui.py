from email.mime import image
from tkinter import *
from turtle import onclick
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:


    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)

        self.score_label = Label(text = "Score: 0", fg = "white", bg = THEME_COLOR)

        self.canvas = Canvas(width = 300, height = 250, bg = 'white')
        self.question_text = self.canvas.create_text(150, 125, width = 280, text = " ", fill = THEME_COLOR, font = ("Helvetica", 20))
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image = true_img, highlightthickness=0, command = self.true_pressed)
        self.true_button.grid(row = 2, column = 0)
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(row = 2, column = 1, command = self.false_pressed)
        self.false_button.grid(row = 2, column = 1)

        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg = 'white')
        if self.quiz.still_has_questions:
            self.score_label.config(text = f"Score: {self.quiz.score}/{self.quiz.question_number}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = question_text)
        else:
            self.canvas.config(bg = 'grey')
            self.canvas.itemconfig(self.question_text, text = "You've completed the quiz")
            self.score_label.config(text = f"Score: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_pressed(self):
        outcome = self.quiz.check_answer('True')
        self.give_feedback(outcome)


    def false_pressed(self):
        outcome = self.quiz.check_answer('False')
        self.give_feedback(outcome)

    def give_feedback(self, outcome):
        if outcome == True:
            self.canvas.config(bg = 'green')
            self.window.after(1000, self.get_next_question)
        if outcome == False:
            self.canvas.config(bg = 'red')
            self.window.after(1000, self.get_next_question)
            