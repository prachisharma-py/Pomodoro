from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
PURPLE = "#774360"
NEON = "#143F6B"
YELLOW = "#FAC213"
FONT_NAME = "Brush Script MT"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    time_label.config(text="Timer", fg=PURPLE, bg=PINK, font=(FONT_NAME, 50, "bold"))
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        time_label.config(text="Break", fg=YELLOW, bg=PINK, font=(FONT_NAME, 50, "bold"))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        time_label.config(text="Break", fg=NEON, bg=PINK, font=(FONT_NAME, 50, "bold"))
    else:
        count_down(work_sec)
        time_label.config(text="Work", fg=PURPLE, bg=PINK, font=(FONT_NAME, 50, "bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PINK)

canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file="image/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

time_label = Label(text="Timer", fg=PURPLE, bg=PINK, font=(FONT_NAME, 50, "bold"))
time_label.grid(column=2, row=1)

start_button = Button(text="Start", highlightthickness=0,  fg=PURPLE, bg=PINK,
                      font=(FONT_NAME, 30, "bold"), command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, fg=PURPLE, bg=PINK,
                      font=(FONT_NAME, 30, "bold"), command=reset_timer)
reset_button.grid(column=3, row=3)

check_marks = Label(fg=NEON, bg=PINK, font=(FONT_NAME, 30, "bold"))
check_marks.grid(column=2, row=3)

window.mainloop()
