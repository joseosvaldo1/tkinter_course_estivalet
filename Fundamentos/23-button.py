import tkinter as tk
from tkinter import ttk

# Create the root window:
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Button Demo')

# Exit button:
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button.pack(ipadx=5, ipady=5,expand=True)

root.mainloop()


# Sintaxe para os buttons:
# button = ttk.Button(container, **options).
# Uso típico: ttk.Button(container, text, command)
