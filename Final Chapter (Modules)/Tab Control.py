# Iin this topic we will discuss about tab control (Ntebook)
import tkinter as tk
from tkinter import Grid, ttk

win = tk.Tk()
win.title("Notebook Page/Tab")

# Here we can create our notebook window
nb = ttk.Notebook(win)

# After notebook we create the pages hoe much pages/tab we want
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)

# Here we add our pages/tab into the notebook
nb.add(page1, text="Page 1")
nb.add(page2, text="Page 2")
nb.pack(expand=True, fill=tk.BOTH)

# Here we add some widget to our notebook
page1_label = ttk.Label(page1, text="This is Labal : ")
page1_label.grid(row=0, column=0, pady=1)

page1_entry = ttk.Entry(page1, width=16)
page1_entry.grid(row=0, column=1, pady=2)



win.mainloop()