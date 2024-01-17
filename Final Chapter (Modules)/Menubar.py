# In this topic we will learn about menubar. That how we can create a menubar
import tkinter as tk
from tkinter import  ttk

win = tk.Tk()
win.title("Menubar")

# 1. Single Menubar
# s_menu = tk.Menu(win)
# s_menu.add_command(label="File")
# s_menu.add_command(label="Edit")
# s_menu.add_command(label="View")

# # Adding to the window
# win.config(menu=s_menu)


# 2. Drop Down Menu
main_menu = tk.Menu(win)

# File Menu
file_menu = tk.Menu(main_menu, tearoff=0)
# Adding Button
file_menu.add_command(label="Open")
file_menu.add_command(label="New Window")
file_menu.add_separator()    # For adding Lines for separating
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As")
# Adding our menu to the main menu
main_menu.add_cascade(menu=file_menu, label="File")


# Edit Menu
edit_menu = tk.Menu(main_menu, tearoff=0)
# Adding Button
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_separator()    # For adding Lines for separating
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
edit_menu.add_separator()
edit_menu.add_command(label="Find")
edit_menu.add_command(label="Replace")
# Adding our menu to the main menu
main_menu.add_cascade(menu=edit_menu, label="Edit")





# Adding our menu to the main wnindow
win.config(menu=main_menu)
win.mainloop()