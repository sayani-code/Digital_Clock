import tkinter as tk
from time import strftime

root=tk.Tk()
root.title("Digital Clock")
root.geometry("100x50")
root.configure(bg="#c3cbb6")

def display():

    string=strftime("%H : %M : %S %p \n")
    current_date = strftime("%A, %d %B %Y")
    label.config(text=[string,current_date])
   
    label.after(1000,display)
    
label=tk.Label(root,font=("calibri",30,'bold'),background="#c3cbb6",foreground="#0B3C8A")
label.pack(anchor="center")
time_left=300

def countdown():
    global time_left 
    if time_left>0 :
        min=time_left//60
        sec=time_left%60
        time_text=f"{min:02d}:{sec:02d}"
        label.config(text=time_text)
        label.after(1000,countdown)
        time_left=time_left-1
    else:
        label.config(text="Time Overe!")

label = tk.Label(root, font=('calibri', 100, 'bold'),background='black', foreground='red')
label.pack(anchor='center')
countdown()

display()


root.mainloop()
