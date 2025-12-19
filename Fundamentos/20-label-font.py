import tkinter as tk
from tkinter.ttk import Label

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Label Widget Demo')

# Show a label:
label = Label(
    root, 
    text="This is a label",
    font=("Helvetica", 14))
label.pack(ipadx=10, ipady=10)


root.mainloop()