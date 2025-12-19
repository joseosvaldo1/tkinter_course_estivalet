# Selecionar arquivos:

# # Selecionando um único arquivo:

# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog as fd
# from tkinter.messagebox import showinfo


# # Create the root window:
# root = tk.Tk()
# root.title('Tkinter Open File Dialog')
# root.resizable(False, False)
# root.geometry('300x150')


# def select_file():
#     filetypes = (
#         ('text files', '*.txt'),
#         ('All files', '*.*')
#     )

#     filename = fd.askopenfilename(
#         title='Open a file',
#         # initialdir='/',  # '/' => Indica a pasta raiz do sistema (C:)
#         initialdir='.',  # '.' => Indica a pasta atual.
#         filetypes=filetypes)

#     showinfo(
#         title='Selected File',
#         message=filename
#     )


# # Open button:
# open_button = ttk.Button(
#     root,
#     text='Open a File',
#     command=select_file
# )

# open_button.pack(expand=True)


# # Run the application:
# root.mainloop()

#############################################################################

# Selecionando múltiplos arquivos:

# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog as fd
# from tkinter.messagebox import showinfo

# # Create the root window
# root = tk.Tk()
# root.title('Tkinter File Dialog')
# root.resizable(False, False)
# root.geometry('300x150')


# def select_files():
#     filetypes = (
#         ('text files', '*.txt'),
#         ('All files', '*.*')
#     )

#     filenames = fd.askopenfilenames(
#         title='Open files',
#         initialdir='/',
#         filetypes=filetypes)

#     showinfo(
#         title='Selected Files',
#         message=filenames
#     )


# # Open button:
# open_button = ttk.Button(
#     root,
#     text='Open Files',
#     command=select_files
# )

# open_button.pack(expand=True)


# # Start the app:
# root.mainloop()


#############################################################################

# Askopenfile(s) methods:

# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog as fd

# # Root window:
# root = tk.Tk()
# root.title('Display a Text File')
# root.resizable(False, False)
# root.geometry('550x250')

# # Text editor:
# text = tk.Text(root, height=12)
# text.grid(column=0, row=0, sticky='nsew')


# def open_text_file():
#     # File type:
#     filetypes = (
#         ('text files', '*.txt'),
#         ('All files', '*.*')
#     )
#     # Show the open file dialog:
#     f = fd.askopenfile(filetypes=filetypes)
#     # Read the text file and show its content on the Text:
#     text.insert('1.0', f.readlines())


# # Open file button:
# open_button = ttk.Button(
#     root,
#     text='Open a File',
#     command=open_text_file
# )

# open_button.grid(column=0, row=1, sticky='w', padx=10, pady=10)

# # Start the app:
# root.mainloop()


#############################################################################


import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

# Root window:
root = tk.Tk()
root.title('Display a Text File')
root.resizable(False, False)
root.geometry('550x250')

# Text editor:
text = tk.Text(root, height=12)
text.grid(column=0, row=0, sticky='nsew')


def open_text_file():
    # File type:
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # Show the open file dialog:
    f = fd.askopenfile(filetypes=filetypes)
    # Read the text file and show its content on the Text:
    lines = f.readlines()
    file_content = ''.join(lines)
    text.insert('1.0', file_content)


# Open file button:
open_button = ttk.Button(
    root,
    text='Open a File',
    command=open_text_file
)

open_button.grid(column=0, row=1, sticky='w', padx=10, pady=10)

# Start the app:
root.mainloop()
