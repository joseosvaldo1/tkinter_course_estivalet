## Caixas de confirmação:

# Askyesno:

# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import askyesno

# # Create the root window:
# root = tk.Tk()
# root.title('Tkinter Yes/No Dialog')
# root.geometry('300x150')

# # Click event handler:
# def confirm():
#     answer = askyesno(title='confirmation',
#                       message='Are you sure that you want to quit?')
#     if answer:
#         root.destroy()


# ttk.Button(
#     root,
#     text='Ask Yes/No',
#     command=confirm).pack(expand=True)


# # Start the app:
# root.mainloop()



#############################################################################


# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import askokcancel, showinfo, WARNING

# # Askokcancel:

# # Create the root window:
# root = tk.Tk()
# root.title('Tkinter Ok/Cancel Dialog')
# root.geometry('300x150')

# # Click event handler:
# def confirm():
#     answer = askokcancel(
#         title='Confirmation',
#         message='Deleting will delete all the data.',
#         icon=WARNING)

#     if answer:
#         showinfo(
#             title='Deletion Status',
#             message='The data is deleted successfully')


# ttk.Button(
#     root,
#     text='Delete All',
#     command=confirm).pack(expand=True)


# # Start the app:
# root.mainloop()

#############################################################################

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askretrycancel, showinfo


# Askretrycancel:

# Create the root window:
root = tk.Tk()
root.title('Tkinter OK/Retry Dialog')
root.geometry('300x150')

# Click event handler:
def confirm():
    answer = askretrycancel(
        title='Connection Issue',
        message='The database server is unreachable. Do you want to retry?'
    )
    if answer:
        showinfo(
            title='Information',
            message='Attempt to connect to the database again.')


ttk.Button(
    root,
    text='Connect to the Database Server',
    command=confirm).pack(expand=True)


# Start the app:
root.mainloop()