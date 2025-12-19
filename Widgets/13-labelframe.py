# LabelFrame:
# Sintaxe básica: 
# lf = ttk.LabelFrame(container, **options)

#######################################################################################

# import tkinter as tk
# from tkinter import ttk

# # Root window:
# root = tk.Tk()

# # Configure the root window:
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('LabelFrame Demo')

# # Label frame:
# lf = ttk.LabelFrame(root, text='Alignment')
# lf.grid(column=0, row=0, padx=20, pady=20)

# alignment_var = tk.StringVar()
# alignments = ('Left', 'Center', 'Right')

# # Create radio buttons and place them on the label frame:
# grid_column = 0
# for alignment in alignments:
#     # Create a radio button:
#     radio = ttk.Radiobutton(lf, text=alignment, value=alignment, variable=alignment_var)
#     radio.grid(column=grid_column, row=0, ipadx=10, ipady=10)
#     # Grid column:
#     grid_column += 1

# root.mainloop()

#######################################################################################

import tkinter as tk
from tkinter import ttk

# Root window:
root = tk.Tk()
root.title('LabelFrame Label Anchor')

# Label frame:
lf = ttk.LabelFrame(root, text='Label Anchor')
lf.grid(column=0, row=0, padx=20, pady=20, sticky=tk.NSEW)

anchor_var = tk.StringVar()
anchors = {
    'nw': {'row': 0, 'column': 1},
    'n': {'row': 0, 'column': 2},
    'ne': {'row': 0, 'column': 3},
    'en': {'row': 1, 'column': 4},
    'e': {'row': 2, 'column': 4},
    'es': {'row': 3, 'column': 4},
    'se': {'row': 4, 'column': 3},
    's': {'row': 4, 'column': 2},
    'sw': {'row': 4, 'column': 1},
    'ws': {'row': 3, 'column': 0},
    'w': {'row': 2, 'column': 0},
    'wn': {'row': 1, 'column': 0}
}


def change_label_anchor():
    lf['labelanchor'] = anchor_var.get()


# Create radio buttons and place them on the label frame:
for key, value in anchors.items():
    # Create a radio button:
    radio = ttk.Radiobutton(
        lf,
        text=key.upper(),
        value=key,
        command=change_label_anchor,
        variable=anchor_var
    ).grid(**value, padx=10, pady=10, sticky=tk.NSEW)

# Set the radio button selected:
anchor_var.set(lf['labelanchor'])

# Show the root window:
root.mainloop()