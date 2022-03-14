from tkinter import *
import math

# CONSTANT
PINK = "#e29779c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "After disaster"
WORK = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


class Pomodoro:
    def __init__(self):
        self.window = Tk()
        self.Image = PhotoImage(file="./Images/tomato.png")
        self.canvas = Canvas(width=292, height=300, bg = YELLOW, highlightthickness=0)
        self.canvas.create_image(146, 150, image = self.Image)
        self.timer = self.canvas.create_text(146, 240, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
        self.canvas.grid(row=1, column=1)
        self.window.title("Pomodoro")
        self.window_configuration()
        self.text_configuration()
        self.window.mainloop()

    def window_configuration(self):
        """Sets the padding horizontally and vertically"""
        self.window.config(padx=50, pady=40, bg=YELLOW)

    def text_configuration(self):
        timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
        timer_label.grid(row=0, column=1)

        start_text = Button(text="Start", fg=GREEN, bg=YELLOW, font=("Bahnschrift", 10), command=self.trigger_count_down)
        start_text.grid(row=2, column=0)

        reset_text = Button(text="Reset", fg=GREEN, bg=YELLOW, font=("Bahnschrift", 10))
        reset_text.grid(row=2, column=2)

        check_text = Label(text="✔", fg=GREEN, bg=YELLOW)
        check_text.grid(row=2, column=1)

    def count_down(self, count):
        """This functions is to change the timer tex and modifying text as well"""
        counter_minutes = math.floor(count/60)
        counter_seconds = count % 60

        self.canvas.itemconfig(self.timer, text=f"{counter_minutes}:{counter_seconds}")
        if count > 0:
            self.window.after(1000, self.count_down, count-1)
        else:
            print("Time's UP!")

    def trigger_count_down(self):
        self.count_down(25*60)


if __name__ == "__main__":
    window = Pomodoro()