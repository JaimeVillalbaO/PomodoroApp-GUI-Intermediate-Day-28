from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_list = []
check = ''
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    # timer text 00:00
    canvas.itemconfig(timer_text, text='00:00')
    # titlle 'timer'
    tittle_label.config(text='Timer')
    # reset checkmark
    chech_marks.config(text='')
    global reps, check
    reps = 0
    check = ''


# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, background=YELLOW)


def timer_count(count):
    count_min = int(count / 60)
    count_sec = str(count % 60)
    if len(count_sec)==1:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer        
        timer = window.after(1000, timer_count, count-1)
    else:
        init_count()
        
 
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)



def init_count():
    global reps
    global check_list
    global check
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        timer_count(work_sec)
        tittle_label.config(text='Work', fg= GREEN)
        
        check_list.append(check)
        check_str = ''.join(check_list)
        chech_marks.config(text=check_str)
        check = ' ✓'



    elif reps == 2 or reps == 4 or reps == 6 or reps == 8:
        timer_count(short_break_sec)
        tittle_label.config(text='Break', fg= PINK)
    elif reps == 9:
        timer_count(long_break_sec)
        tittle_label.config(text='Break', fg= RED)
        check = ' ✓'
        check_list.append(check)
        check_str = ''.join(check_list)
        chech_marks.config(text=check_str)
        
        

tittle_label = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
tittle_label.grid(column=1, row=0)

chech_marks = Label(font=(FONT_NAME, 20, 'normal'), bg=YELLOW, fg=GREEN)
chech_marks.grid(column=1, row=2)

button_star = Button(text='Start', font=(FONT_NAME, 12, 'normal'), command=init_count)
button_star.grid(column=0, row=2)

button_reset = Button(text='Reset', font=(FONT_NAME, 12, 'normal'), command=reset_timer)
button_reset.grid(column=2, row=2)


window.mainloop()
