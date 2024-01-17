# In this topic we will learn how to make an gui application with the help of using different module
# So lets start
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tmsg
import os
from csv import DictWriter

from PIL import Image



win = tk.Tk()
win.wm_title(os.getcwd()+ " - " +"Simple Application")

# Creating Labels
name_label = ttk.Label(win, text="Enter Your Name : ")
name_label.grid(row=0, column=0, sticky=tk.W)

age_label = ttk.Label(win, text="Enter Your Age : ")
age_label.grid(row=1, column=0, sticky=tk.W)

email_label = ttk.Label(win, text="Enter Your Email : ")
email_label.grid(row=2, column=0, sticky=tk.W)

gender_label = ttk.Label(win, text="Select Your Gender : ")
gender_label.grid(row=3, column=0, sticky=tk.W)

# Creating Entries
name_var = tk.StringVar()
name_entry = ttk.Entry(win, width=16, textvariable=name_var)
name_entry.grid(row=0, column=1, pady=1)
name_entry.focus()

age_var = tk.StringVar()
age_entry = ttk.Entry(win, width=16, textvariable=age_var)
age_entry.grid(row=1, column=1, pady=1)

email_var = tk.StringVar()
email_entry = ttk.Entry(win, width=16, textvariable=email_var)
email_entry.grid(row=2, column=1, pady=1)

# Creating combobox
gender_var = tk.StringVar()
gender_combo = ttk.Combobox(win, width=14, textvariable=gender_var, state="readonly")
gender_combo["values"] = ("Male", "Female", "Other")
gender_combo.current(0)
gender_combo.grid(row=3, column=1, pady=1)

# Creating Radio buttons
type_var = tk.StringVar()
type_var.set("Student")
std_btn = ttk.Radiobutton(win, text="Student", value="Student", variable=type_var)
std_btn.grid(row=4, column=0)

tch_btn = ttk.Radiobutton(win, text="Teacher", value="Teacher", variable=type_var)
tch_btn.grid(row=4, column=1)

# Creating Check Button
check_var = tk.IntVar()
sub_btn = ttk.Checkbutton(win, text="Check if you want to subscribe to our newsletter", variable=check_var)
sub_btn.grid(row=5, columnspan=3)


# Button function
def action():
    name = name_var.get()
    age = age_var.get()
    email = email_var.get()
    gender = gender_var.get()
    user_type = type_var.get()
    if check_var.get() == 0:
        sub = "NO"
    else:
        sub = "YES"
    
    # print(name, age, email, gender, user_type, sub)
    with open("Records.csv", "a", newline="", encoding="UTF-8") as f:
        dict_writer = DictWriter(f, fieldnames=["UserName", "UserAge", "UserEmailAddress", "UserGender", "UserType", "Subscription"])
        # Now here is one prolem if we write headers then whenever we click the submit button this creates the new header one by one. For ths this problem we use os module
        if os.stat("Records.csv").st_size == 0:
            dict_writer.writeheader()
        
        dict_writer.writerow({
            "UserName": name,
            "UserAge": age,
            "UserEmailAddress": email,
            "UserGender": gender,
            "UserType": user_type,
            "Subscription": sub
        })


    tmsg.showinfo("Submision", "Thank Your Application has been Submitted.")
    # edit_label.configure(text="Submitted", foreground="Green", font="Arial 10 bold")
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)



# Creating Button
submit_btn = ttk.Button(win, text="Submit", width=16, command=action)
submit_btn.grid(row=6, column=0, pady=1)



def help_():
    tmsg.showinfo("Help", "Remember All Field are Required to fill.\n\nFor the better experiecne visit our site.\nwww.aerosoft.com.")

img = tk.PhotoImage(file=r"D:\Courses\Icons\Now Icons\must_have_icon_set\Help\Help_16x16.png")
edit_label = ttk.Button(win, image=img, command=help_)
edit_label.grid(row=6, column=1, sticky=tk.E)



win.mainloop()