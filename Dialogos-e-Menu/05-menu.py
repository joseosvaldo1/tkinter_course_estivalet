# # Menus:


import tkinter as tk
from tkinter import Menu

# Root window:
root = tk.Tk()
root.title('Menu Demo')

# Create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create a menu:
file_menu = Menu(menubar, tearoff=False)

# Add a menu item to the menu:
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Close')
file_menu.add_separator()

# Add a submenu:
sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label='Keyboard Shortcuts')
sub_menu.add_command(label='Color Themes')

# Add the file menu to the menubar:
file_menu.add_cascade(
    label='Preferences',
    menu=sub_menu
)

file_menu.add_separator()

file_menu.add_command(
    label='Exit',
    command=root.destroy
)


# Add the File menu to the menubar:
menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)


# Create the Help Menu:
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

menubar.add_cascade(
    label="Help",
    menu=help_menu,
    underline=0
)


root.mainloop()





