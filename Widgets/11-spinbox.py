# Spinbox:
# Sintaxe básica: 
# ttk.Spinbox(container, from initial_value, to final_value, textvariable, wrap)

#######################################################################################

# import tkinter as tk
# from tkinter import ttk


# # Root window:
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Spinbox Demo')

# # Spinbox:
# current_value = tk.StringVar(value=0)
# spin_box = ttk.Spinbox(
#     root,
#     from_=0,
#     to=30,
#     textvariable=current_value,
#     wrap=True)

# spin_box.pack()

# root.mainloop()


#######################################################################################

import tkinter as tk
from tkinter import ttk


# Root window:
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Spinbox Demo')


# Spinbox:
current_value = tk.StringVar()
spin_box = ttk.Spinbox(
    root,
    from_=0,
    to=50,
    values=(0, 10, 20, 30, 40, 50),
    textvariable=current_value,
    wrap=True)

spin_box.pack()

root.mainloop()