import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import pytz


# Main Window
root = tk.Tk()
root.title("Advanced Digital Clock")
root.geometry("550x650")

bg_dark = "#161D3D"
fg_dark = "white"

bg_light = "white"
fg_light = "black"

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

update_clock()

root.mainloop()