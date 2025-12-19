# Checkbox:
# Sintaxe básica:

# checkbox_var = tk.StringVar()


# def check_changed():
#     # ...


# checkbox = ttk.Checkbutton(
#     container,
#     text='<checkbox label>',
#     command=check_changed,
#     variable=checkbox_var,
#     onvalue='<value_when_checked>',
#     offvalue='<value_when_unchecked>'
# )


###################################################################

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Checkbox Demo')

agreement = tk.StringVar()


def agreement_changed():
    tk.messagebox.showinfo(title='Result', message=agreement.get())


ttk.Checkbutton(root,
                text='I agree',
                command=agreement_changed,
                variable=agreement,
                onvalue='agree',
                offvalue='disagree').pack()


root.mainloop()