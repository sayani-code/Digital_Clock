import tkinter as tk
from time import strftime

root=tk.Tk()
root.title("Digital Clock")
root.geometry("600x200")
root.configure(bg="#c3cbb6")

def display():

    string=strftime("%H : %M : %S %p \n %D")
    label.config(text=string)
    label.after(1000,display)
    
label=tk.Label(root,font=("calibri",30,'bold'),background="#c3cbb6",foreground="#0B3C8A")
label.pack(anchor="center")

display()


root.mainloop()
