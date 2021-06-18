from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None                             

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    timer_label.config(text = "TIMER")
    check_mark.config(text = "")
    global reps
    reps = 0                            


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text = "Long Break", fg = RED)

    elif reps % 2 != 0:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg = GREEN)

    else:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text = "Short Break", fg = PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    count_min = count//60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text , text = f"{count_min}:{count_sec}")

    if(count > 0):
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()

        marks = ""
        total_worksessions = reps//2                   
        for i in range(total_worksessions):
            marks += "✔"
        check_mark.config(text = marks)



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer")
window.config(padx = 100, pady = 50, bg = YELLOW)


timer_label = Label(text = "Timer", fg = GREEN, bg = YELLOW, font = ("Courier", 50, "bold"))
timer_label.grid(row= 0, column= 1)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image= tomato_img)      # x= 100, y= 112

timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = ("Courier", 35, "bold"))
canvas.grid(row = 1, column = 1)


start_button = Button(text = "Start", highlightthickness = 0, command = start_timer)
start_button.grid(row = 2, column = 0)

reset_button = Button(text= "Reset", highlightthickness = 0, command = reset_timer)
reset_button.grid(row= 2, column =2)

check_mark = Label(fg = RED, bg = YELLOW)
check_mark.grid(row = 3, column = 1)



window.mainloop()

# Application by Shivani Verma
