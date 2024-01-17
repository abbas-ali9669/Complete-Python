# In this topic we will learn abut labelframe that we can add our widget into the frame for better looking

import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Padding and Label Frame")

label_frame = ttk.LabelFrame(win, borderwidth=4, relief="sunken")
label_frame.grid(row=0, column=0, pady=2, padx=4)


labels = ("Enter Your Name : ", "Enter Your Age : ", "Enter Your Country : ", "Enter Your State : ", "Enter Your Address : ")

for i in range(len(labels)):
    cur_label = "label" + str(i)
    cur_label = ttk.Label(label_frame, text=labels[i])
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
    cur_entry = ttk.Entry(label_frame, width=16, textvariable=user_info[i])
    cur_entry.grid(column=1, row=counter)
    counter += 1


def action():
    print(user_info['name'].get())
    print(user_info.get('age').get())
    print(user_info["Country"].get())
    print(user_info['State'].get())
    print(user_info["Address"].get())

sub_btn = ttk.Button(win, text="Submit",width=15, command=action)
sub_btn.grid(row=1, columnspan=2)

# Now here we have a method for giving padding to our widget
for child in label_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)
    # Here we can give our widget padding


win.mainloop()