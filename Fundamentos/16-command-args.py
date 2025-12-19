import tkinter as tk
from tkinter import ttk

root = tk.Tk()


def select(option):
    print(option)


button = ttk.Button(root, text="Rock", command=lambda: select("Rock selected")).pack()
button = ttk.Button(root, text="Paper", command=lambda: select("Paper selected")).pack()
button = ttk.Button(root, text="Scissors", command=lambda: select("Scissors selected")).pack()

root.mainloop()