from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some question text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        correct_button_img = PhotoImage(file="images/true.png")
        correct_button = Button(image=correct_button_img, highlightthickness=0)
        correct_button.grid(row=2, column=0)
        wrong_button_img = PhotoImage(file="images/false.png")
        wrong_button = Button(image=wrong_button_img, highlightthickness=0)
        wrong_button.grid(row=2, column=1)

        score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        score_label.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)