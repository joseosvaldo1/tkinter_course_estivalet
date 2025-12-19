# Sizegrip:

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Sizegrip Demo')
root.geometry('300x200')
root.resizable(True, True)

# Grid layout:
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create the sizegrip:
sg = ttk.Sizegrip(root)
sg.grid(row=1, sticky=tk.SE)


root.mainloop()