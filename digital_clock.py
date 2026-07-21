import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import pytz
import winsound

# =========================
# Main Window
# =========================

root = tk.Tk()
root.title("Advanced Digital Clock")
root.geometry("700x550")
root.resizable(False, False)

# =========================
# Theme
# =========================

dark_mode = True

bg_dark = "#161D3D"
fg_dark = "#FFFFFF"

bg_light = "#F5F5F5"
fg_light = "#111111"

root.configure(bg=bg_dark)

# =========================
# Clock
# =========================

time_label = tk.Label(
    root,
    font=("Arial", 40, "bold"),
    bg=bg_dark,
    fg=fg_dark
)
time_label.pack(pady=10)

date_label = tk.Label(
    root,
    font=("Arial", 18),
    bg=bg_dark,
    fg=fg_dark
)
date_label.pack()

zones = [
    "Asia/Kolkata",
    "UTC",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney"
]

timezone = ttk.Combobox(root, values=zones, width=25)
timezone.current(0)
timezone.pack(pady=5)

# =========================
# Alarm Variables
# =========================

alarm_time = ""
alarm_running = False

# =========================
# Clock Update
# =========================

def update_clock():

    global alarm_running

    tz = pytz.timezone(timezone.get())
    now = datetime.now(tz)

    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%A, %d %B %Y")

    time_label.config(text=current_time)
    date_label.config(text=current_date)

    if alarm_running and current_time == alarm_time:
        winsound.Beep(1200, 1000)
        messagebox.showinfo("Alarm", "Wake Up!")
        cancel_alarm()

    root.after(1000, update_clock)

# =========================
# Theme Change
# =========================

def toggle_theme():

    global dark_mode

    dark_mode = not dark_mode

    if dark_mode:
        bg = bg_dark
        fg = fg_dark
    else:
        bg = bg_light
        fg = fg_light

    root.configure(bg=bg)

    widgets = root.winfo_children()

    for widget in widgets:
        try:
            widget.configure(bg=bg, fg=fg)
        except:
            pass

    for frame in [features_frame, timer_frame, stop_frame, alarm_frame]:
        frame.configure(bg=bg)

    for lbl in all_labels:
        lbl.configure(bg=bg, fg=fg)

# =========================
# Button
# =========================

tk.Button(
    root,
    text="Mode Change",
    command=toggle_theme
).pack(pady=10)

# =========================
# Frames
# =========================

features_frame = tk.Frame(root, bg=bg_dark)
features_frame.pack(pady=20)

timer_frame = tk.Frame(features_frame, bg=bg_dark)
timer_frame.grid(row=0, column=0, padx=25)

stop_frame = tk.Frame(features_frame, bg=bg_dark)
stop_frame.grid(row=0, column=1, padx=25)

alarm_frame = tk.Frame(features_frame, bg=bg_dark)
alarm_frame.grid(row=0, column=2, padx=25)

all_labels = []

# ====================================================
# TIMER
# ====================================================

timer_running = False
timer_seconds = 0

timer_title = tk.Label(timer_frame,
                       text="Timer",
                       bg=bg_dark,
                       fg=fg_dark,
                       font=("Arial",14))

timer_title.pack()

all_labels.append(timer_title)

timer_label = tk.Label(timer_frame,
                       text="00:00:00",
                       font=("Arial",18),
                       bg=bg_dark,
                       fg=fg_dark)

timer_label.pack()

all_labels.append(timer_label)

timer_entry = tk.Entry(timer_frame,width=10)
timer_entry.pack(pady=5)
timer_entry.insert(0,"60")

def update_timer():

    global timer_seconds

    if timer_running:

        if timer_seconds>0:

            timer_seconds-=1

            h=timer_seconds//3600
            m=(timer_seconds%3600)//60
            s=timer_seconds%60

            timer_label.config(text=f"{h:02}:{m:02}:{s:02}")

        else:

            stop_timer()

            winsound.Beep(1000,1000)

            messagebox.showinfo("Timer","Time Up!")

    root.after(1000,update_timer)

def start_timer():

    global timer_running,timer_seconds

    if timer_seconds==0:
        try:
            timer_seconds=int(timer_entry.get())
        except:
            messagebox.showerror("Error","Enter seconds only.")
            return

    timer_running=True

def stop_timer():

    global timer_running

    timer_running=False

def reset_timer():

    global timer_running,timer_seconds

    timer_running=False
    timer_seconds=0

    timer_label.config(text="00:00:00")

tk.Button(timer_frame,text="Start",command=start_timer).pack(fill="x")
tk.Button(timer_frame,text="Stop",command=stop_timer).pack(fill="x")
tk.Button(timer_frame,text="Reset",command=reset_timer).pack(fill="x")

# ====================================================
# STOPWATCH
# ====================================================

stopwatch_running=False
stopwatch_seconds=0

stop_title=tk.Label(stop_frame,
                    text="Stopwatch",
                    bg=bg_dark,
                    fg=fg_dark,
                    font=("Arial",14))

stop_title.pack()

all_labels.append(stop_title)

stopwatch_label=tk.Label(stop_frame,
                         text="00:00:00",
                         font=("Arial",18),
                         bg=bg_dark,
                         fg=fg_dark)

stopwatch_label.pack()

all_labels.append(stopwatch_label)

def update_stopwatch():

    global stopwatch_seconds

    if stopwatch_running:

        stopwatch_seconds+=1

        h=stopwatch_seconds//3600
        m=(stopwatch_seconds%3600)//60
        s=stopwatch_seconds%60

        stopwatch_label.config(text=f"{h:02}:{m:02}:{s:02}")

    root.after(1000,update_stopwatch)

def start_stopwatch():

    global stopwatch_running

    stopwatch_running=True

def stop_stopwatch():

    global stopwatch_running

    stopwatch_running=False

def reset_stopwatch():

    global stopwatch_seconds

    stopwatch_seconds=0

    stopwatch_label.config(text="00:00:00")

tk.Button(stop_frame,text="Start",command=start_stopwatch).pack(fill="x")
tk.Button(stop_frame,text="Stop",command=stop_stopwatch).pack(fill="x")
tk.Button(stop_frame,text="Reset",command=reset_stopwatch).pack(fill="x")

# ====================================================
# ALARM
# ====================================================

alarm_title=tk.Label(alarm_frame,
                     text="Alarm",
                     bg=bg_dark,
                     fg=fg_dark,
                     font=("Arial",14))

alarm_title.pack()

all_labels.append(alarm_title)

alarm_entry=tk.Entry(alarm_frame,width=10)
alarm_entry.pack(pady=5)
alarm_entry.insert(0,"07:30:00")

alarm_status=tk.Label(alarm_frame,
                      text="No Alarm",
                      bg=bg_dark,
                      fg=fg_dark)

alarm_status.pack()

all_labels.append(alarm_status)

def set_alarm():

    global alarm_time,alarm_running

    alarm_time=alarm_entry.get()

    alarm_running=True

    alarm_status.config(text="Alarm Set")

def cancel_alarm():

    global alarm_running

    alarm_running=False

    alarm_status.config(text="Cancelled")

tk.Button(alarm_frame,
          text="Set Alarm",
          command=set_alarm).pack(fill="x")

tk.Button(alarm_frame,
          text="Cancel",
          command=cancel_alarm).pack(fill="x")

# ====================================================
# Start
# ====================================================

update_clock()
update_stopwatch()
update_timer()

root.mainloop()