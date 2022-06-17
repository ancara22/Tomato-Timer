from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


window = Tk()
window.title("Tomato Timer")
window.config(padx=150, pady=100, bg=YELLOW, )

text_label = Label(text="Timer", bg=YELLOW, fg=GREEN, pady=20, font=(FONT_NAME, 36, "normal"))
text_label.grid(column=2, row=0)

img = PhotoImage(file="tomato.png")
canvas = Canvas(bg=YELLOW, highlightthickness=0, width=200, height=250)
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text=f"0:0", fill="white", font=(FONT_NAME, 26, "normal"))
canvas.grid(column=2, row=1)


def add_gal():
    global reps
    count = int(reps/2)
    txt = ""
    for i in range(0, count):
        txt += "✓ "
    gal_label.config(text=f"{txt}")


def start():
    global reps
    reps += 1
    add_gal()

    if reps % 8 == 0:
        countdown(20 * 60)
        text_label.config(text="Brake", fg=PINK)
    elif reps % 2 == 0:
        countdown(5 * 60)
        text_label.config(text="Brake", fg=GREEN)
    else:
        countdown(25 * 60)
        text_label.config(text="Work", fg=RED)


def reset():
    window.after_cancel(timer)
    text_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="0:0")
    gal_label.config(text=f" ")


def countdown(count):
    global timer
    m = int(count/60)
    s = count % 60
    canvas.itemconfig(timer_text, text=f"{m}:{s}")

    if count > 0:
       timer = window.after(1000, countdown, count - 1)
    else:
        start()


button_start = Button(text="Start", highlightthickness=0, command=start, height=2)
button_start.grid(column=0, row=3)
button_rest = Button(text="Reset", command=reset, highlightthickness=0, height=2)
button_rest.grid(column=3, row=3)
gal_label = Label(text=" ", bg=YELLOW, fg=GREEN, pady=20,)
gal_label.grid(column=2, row=3)


window.mainloop()

