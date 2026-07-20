import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import pytz


# Main Window
root = tk.Tk()
root.title("Advanced Digital Clock")
root.geometry("550x650")

dark_mode = True
bg_dark = "#161D3D"
fg_dark = "#bfaaaa"

bg_light = "#d9dbc6"
fg_light = "#061937"


root.configure(bg=bg_dark)


#Current Time and Date 
time_label = tk.Label(root, font=("Arial", 40, "bold"),
                      bg=bg_dark, fg=fg_dark)
time_label.pack(pady=10)

date_label = tk.Label(root, font=("Arial", 16),
                      bg=bg_dark, fg=fg_dark)
date_label.pack()

zones = [
    "Asia/Kolkata",
    "UTC",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney"
]

timezone = ttk.Combobox(root, values=zones, width=30)
timezone.current(0)
timezone.pack()

def update_clock():
    tz = pytz.timezone(timezone.get())
    now = datetime.now(tz)

    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%A, %d %B %Y")

    time_label.config(text=current_time)
    date_label.config(text=current_date)

    root.after(1000, update_clock)

#Mode change future

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

tk.Button(root,
          text="Mode Change",
          command=toggle_theme).pack(pady=10)


# Stopwatch

stopwatch_running = False
stopwatch_seconds = 0


def update_stopwatch():
    global stopwatch_seconds

    if stopwatch_running:
        stopwatch_seconds += 1

        hrs = stopwatch_seconds // 3600
        mins = (stopwatch_seconds % 3600) // 60
        secs = stopwatch_seconds % 60

        stopwatch_label.config(
            text=f"{hrs:02}:{mins:02}:{secs:02}")

    root.after(1000, update_stopwatch)


def start_stopwatch():
    global stopwatch_running
    stopwatch_running = True


def stop_stopwatch():
    global stopwatch_running
    stopwatch_running = False


def reset_stopwatch():
    global stopwatch_seconds
    stopwatch_seconds = 0
    stopwatch_label.config(text="00:00:00")


tk.Label(root,
         text="Stopwatch",
         bg=bg_dark,
         fg=fg_dark,
         font=("Arial", 14)).pack(pady=10)

stopwatch_label = tk.Label(root,
                           text="00:00:00",
                           font=("Arial", 22),
                           bg=bg_dark,
                           fg=fg_dark)
stopwatch_label.pack()

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Start",
          command=start_stopwatch).grid(row=0, column=0)

tk.Button(frame, text="Stop",
          command=stop_stopwatch).grid(row=0, column=1)

tk.Button(frame, text="Reset",
          command=reset_stopwatch).grid(row=0, column=2)


update_clock()
toggle_theme()
update_stopwatch()
start_stopwatch()
stop_stopwatch()
reset_stopwatch()


root.mainloop()