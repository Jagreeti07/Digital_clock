import tkinter as tk
from time import strftime 

root = tk.Tk()
root.title("Digital Clock")

def update_time():
    current_time = strftime("%H:%M:%S %p \n %d-%m-%Y")
    label.config(text=current_time)
    label.after(1000, update_time)

label = tk.Label(root, font=("Arial", 20))
label.pack(pady=20)

update_time()

root.mainloop()