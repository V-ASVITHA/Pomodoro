from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = "Courier"
WORK = 25
SHORT = 5
LONG = 20
reps = 1
tick = ""
timer = None
def count(ct):
    min = math.floor(ct / 60)
    sec = ct % 60
    if sec == 0:
        canvas.itemconfig(tim, text=f"{min}:00")
    elif sec < 10:
        canvas.itemconfig(tim, text=f"{min}:0{sec}")
    else:
        canvas.itemconfig(tim, text=f"{min}:{sec}")
    if ct > 0 :
        global timer
        timer = window.after(1000, count, ct - 1)
    else:
        start()

def start():
    global reps
    global tick
    if reps % 2 == 0 and reps % 10 != 0:
        count(SHORT * 60)
        label.config(text="Short Break", fg=RED)
        tick += "✔️"
        label1.config(text=tick)
    elif reps % 9 == 0 :
        count(LONG * 60)
        label.config(text="Long Break", fg=RED)
    else:
        count(WORK * 60)
        label.config(text="Work", fg=PINK)
    reps += 1

def reset():
    global tick
    global reps
    reps = 1
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(tim, text="00:00")
    tick = ""
    label1.config(text=tick)
    window.after_cancel(timer)

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer",font=(FONT, 30, "bold"), bg=YELLOW, fg=GREEN)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
tim = canvas.create_text(103, 130, text="00:00",fill="white", font=(FONT, 35, "bold"))
canvas.grid(column=1, row=1)

button1 = Button(text="Start", command=start, font=(FONT, 10, "bold"), fg=RED, bg=GREEN)
button1.grid(column=0, row=2)

button2 = Button(text="Reset", command=reset, font=(FONT, 10, "bold"), fg=RED, bg=GREEN)
button2.grid(column=2, row=2)

label1 = Label(fg=GREEN, bg=YELLOW)
label1.grid(column=1, row=3)

window.mainloop()
