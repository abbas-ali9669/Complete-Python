# In this topic we will learn about meassagebox and exception Handling. That how we can handle the events in our applicaton

from os import name
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg



win = tk.Tk()
win.title("Messagebox and Exception Handling")

# Adding Frame
label_frame = ttk.LabelFrame(win, text="Enter Details", padding=5)
label_frame.pack(padx=15, pady=17)

# Adding Details in Frames (Labels)
name_label = ttk.Label(label_frame, text="Enter Your Name : ", font=("Arial", 11, "bold"))
name_label.grid(row=0, column=0, sticky=tk.W, padx=2)

age_label = ttk.Label(label_frame, text="Enter Your Age : ", font=("Arial", 11, "bold"))
age_label.grid(row=0, column=1, sticky=tk.W, padx=2)

# # Adding Details in Frames (Entries)
# Entries var
name_var = tk.StringVar()
age_var = tk.StringVar()

name_entry = ttk.Entry(label_frame, width=28, textvariable=name_var)
name_entry.grid(row=1, column=0, padx=2, pady=5)

age_entry = ttk.Entry(label_frame, width=28, textvariable=age_var)
age_entry.grid(row=1, column=1, padx=2, pady=5)


# Button Func
def action():
    name = name_var.get()
    age = age_var.get()
    if name == "" or age == "":
        msg.showwarning("Field", "All Fields are Required to fill.")
    else:
        try:
            age = int(age)
        except ValueError:
            msg.showerror("Wrong Input", "Please Enter Integer Number\nNumber Require.")
        except:
            msg.showerror("Error", "Unexpected Error.")
        else:
            print(f"{name} : {age}")
            name_entry.delete(0, tk.END)
            age_entry.delete(0, tk.END)
            pass


# Submit Button

sb_btn = ttk.Button(label_frame, text="Submit", width=13, command=action)
sb_btn.grid(columnspan=2)



win.mainloop()