import tkinter as tk
from tkinter import ttk
import os

win = tk.Tk()
win.title(os.getcwd()+" - "+ "tkinter GUI")
win.geometry("700x400")

# Frames
frame_1 = tk.Frame(win, borderwidth=2, relief="ridge", pady=5, padx=5)
frame_1.grid(row=0, column=0, padx=210, pady=5)

# Label
num_1 = ttk.Label(frame_1, text="Enter First Number : ")
num_1.grid(row=0, column=0)

num_2 = ttk.Label(frame_1, text="Enter First Number : ")
num_2.grid(row=1, column=0)

num_3 = ttk.Label(frame_1, text="Output : ")
num_3.grid(row=2, column=0, sticky="w")

# Entry
num_1_entry_var = tk.IntVar()
num_1_entry = ttk.Entry(frame_1, width=16, textvariable=num_1_entry_var)
num_1_entry.grid(row=0, column=1, pady=1)
num_1_entry.focus()

num_2_entry_var = tk.IntVar()
num_2_entry = ttk.Entry(frame_1, width=16, textvariable=num_2_entry_var)
num_2_entry.grid(row=1, column=1, pady=1)


num_3_entry = ttk.Entry(frame_1, width=16, state='readonly')
num_3_entry.grid(row=2, column=1, pady=1)

# Button
def add():
    entry_1 = num_1_entry_var.get()
    entry_2 = num_2_entry_var.get()
    total = entry_1 + entry_2
    # print(total)
    num_3_entry.config(text=total)


add_btn = ttk.Button(frame_1, text="Addition", width=16, command=add)
add_btn.grid(row=3, column=0)

def subtract():
    entry_1 = num_1_entry_var.get()
    entry_2 = num_2_entry_var.get()
    print(entry_1 - entry_2)


sub_btn = ttk.Button(frame_1, text="Substraction", width=16, command=subtract)
sub_btn.grid(row=3, column=1, pady=2)

def multiply():
    entry_1 = num_1_entry_var.get()
    entry_2 = num_2_entry_var.get()
    print(entry_1 * entry_2)

mul_btn = ttk.Button(frame_1, text="Multiply", width=16, command=multiply)
mul_btn.grid(row=4, column=0)

def div():
    entry_1 = num_1_entry_var.get()
    entry_2 = num_2_entry_var.get()
    print(entry_1 / entry_2)

div_btn = ttk.Button(frame_1, text="Divison", width=16, command=div)
div_btn.grid(row=4, column=1)


win.mainloop()