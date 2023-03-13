from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN =  1       #25
SHORT_BREAK_MIN = 1   # 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_Label.config(text="Timer")
    checkBox.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        count_down(long_break_sec)
        timer_Label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_Label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_Label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec<10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        checkBox.config(text=mark)
    
    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)      #Window settings.


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)       #canvas settings.
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

#timer label.
timer_Label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW,)
timer_Label.grid(row=0, column=1)

#Start Button.
start_button = Button(text="Start", font=("Arial", 15), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

#Rest Button.
reset_button = Button(text="Reset", font=("Arial", 15), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

#checkmark label.
checkBox = Label(fg=GREEN, bg=YELLOW)
checkBox.grid(row=3, column=1)


window.mainloop()
