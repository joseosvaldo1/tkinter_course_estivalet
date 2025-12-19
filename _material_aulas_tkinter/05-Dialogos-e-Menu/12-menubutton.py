import tkinter as tk
from tkinter import ttk

def menu_item_selected(*args):
    """ handle menu selected event """
    root.config(bg=selected_color.get())

# root window
root = tk.Tk()
root.geometry('300x250')
root.title('Menubutton Demo')

selected_color = tk.StringVar()
selected_color.trace("w", menu_item_selected)

# create the menu button
colors = ('Red', 'Green', 'Blue')

# create the Menubutton
menu_button = ttk.Menubutton(
    root,
    text='Select a color')

# create a new menu instance
menu = tk.Menu(menu_button, tearoff=0)

for color in colors:
    menu.add_radiobutton(
        label=color,
        value=color,
        variable=selected_color)

# associate menu with the Menubutton
menu_button["menu"] = menu

menu_button.pack(expand=True)

root.mainloop()