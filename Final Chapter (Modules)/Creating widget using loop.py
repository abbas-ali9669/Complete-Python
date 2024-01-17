# In this course we will learn about how to make widget using loop
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Widget Using Loop")

labels = ("Enter Your Name : ", "Enter Your Age : ", "Enter Your Country : ", "Enter Your State : ", "Enter Your Address : ")

for i in range(len(labels)):
    cur_label = "label" + str(i)
    cur_label = ttk.Label(win, text=labels[i])
    cur_label.grid(row=i, column=0, sticky=tk.W)


user_info = {
    "name": tk.StringVar(),
    "age": tk.StringVar(),
    "Country":tk.StringVar(),
    "State":tk.StringVar(),
    "Address":tk.StringVar()
}


counter = 0
for i in user_info:
    cur_entry = "entry" + i
    cur_entry = ttk.Entry(win, width=16, textvariable=user_info[i])
    cur_entry.grid(column=1, row=counter, pady=1)
    counter += 1


def action():
    print(user_info['name'].get())
    print(user_info.get('age').get())
    print(user_info["Country"].get())
    print(user_info['State'].get())
    print(user_info["Address"].get())

sub_btn = ttk.Button(win, text="Submit",width=15, command=action)
sub_btn.grid(row=6, columnspan=2)




win.mainloop()