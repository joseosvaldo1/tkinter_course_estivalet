import tkinter as tk
from tkinter import ttk

def option_changed(*args):
    output_label['text'] = f'You selected: {option_var.get()}'

# root window
root = tk.Tk()
root.geometry('300x250')
root.title('Tkinter OptionMenu Widget')
languages = ('Python', 'JavaScript', 'Java',
                'Swift', 'GoLang', 'C#', 'C++', 'Scala')

option_var = tk.StringVar()

# padding for widgets using the grid layout
paddings = {'padx': 5, 'pady': 5}

# label
label = ttk.Label(text='Select your most favorite language:')
label.grid(column=0, row=0, sticky=tk.W, **paddings)

# option menu
option_menu = ttk.OptionMenu(
    root,
    option_var,
    languages[0],
    *languages,
    command=option_changed)

option_menu.grid(column=1, row=0, sticky=tk.W, **paddings)

# output label
output_label = ttk.Label(root, foreground='red')
output_label.grid(column=0, row=1, sticky=tk.W, **paddings)
root.mainloop()