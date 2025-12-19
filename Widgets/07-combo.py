# Combobox:
# Sintaxe básica:
# current_var = tk.StringVar()
# combobox = ttk.Combobox(container, textvariable=current_var)

# combobox['values'] = ("value1", "value2", "value3")

# combobox['state'] = 'readonly'  # => Não permite valor editável
# combobox['state'] = 'normal'  # => Permite valor editável (padrão)

# combobox.bind('<<ComboboxSelected>>', callback)

#######################################################################################

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name
from datetime import datetime

# Create root window:
root = tk.Tk()

# Config the root window:
root.geometry('300x200')
root.resizable(False, False)
root.title('Combobox Widget')

# Label:
label = ttk.Label(text="Please select a month:")
label.pack(fill=tk.X, padx=5, pady=5)

# Create a combobox:
selected_month = tk.StringVar()
month_cb = ttk.Combobox(root, textvariable=selected_month)

# Get first 3 letters of every month name:
month_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]

# Prevent typing a value:
month_cb['state'] = 'readonly'

# Set the current month
# current_month = datetime.now().strftime('%b')
# month_cb.set(current_month)


# Place the widget
month_cb.pack(fill=tk.X, padx=5, pady=5)


# Bind the selected value changes
def month_changed(event):
    """ Handle the month changed event. """
    showinfo(
        title='Result',
        message=f'You selected {selected_month.get()}!'
    )

month_cb.bind('<<ComboboxSelected>>', month_changed)

# Set the current month:
current_month = datetime.now().strftime('%b')
month_cb.set(current_month)

root.mainloop()