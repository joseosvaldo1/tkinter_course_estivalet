import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Label Widget Demo')

frame = ttk.Frame(root)
frame.columnconfigure(0, weight=1)
frame['borderwidth'] = 5
frame['relief'] = 'sunken'
label = ttk.Label(frame, text='This is a label').grid(row=0,column=0)
frame.pack()

root.mainloop()