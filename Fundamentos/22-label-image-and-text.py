import tkinter as tk
from tkinter import ttk

# Create the root window:
root = tk.Tk()
root.geometry('400x350')
root.resizable(False, False)
root.title('Label Widget Image')

# Display an image label:
photo = tk.PhotoImage(file='./python.png')
image_label = ttk.Label(
    root,
    image=photo,
    padding=5,
    text='Python',
    compound='bottom'
)

image_label.pack()

root.mainloop()