# Notebook:
# Sintaxe básica:
# ttk.Notebook(container, **options)

# options => width, height, padding
# methods => add(child, **kwargs),  hide(tabId),  forget(child)
#                child,
#                text,
#                image,
#                compund,
#                underline,

#######################################################################################

# import tkinter as tk
# from tkinter import ttk

# # Root window:
# root = tk.Tk()
# root.geometry('400x300')
# root.title('Notebook Demo')

# # Create a notebook:
# notebook = ttk.Notebook(root)
# notebook.pack(pady=10, expand=True)

# # Create frames:
# frame1 = ttk.Frame(notebook, width=400, height=280)
# frame2 = ttk.Frame(notebook, width=400, height=280)

# frame1.pack(fill='both', expand=True)
# frame2.pack(fill='both', expand=True)

# # Add frames to notebook:
# notebook.add(frame1, text='General Information')
# notebook.add(frame2, text='Profile')


# root.mainloop()

#######################################################################################

import tkinter as tk
from tkinter import ttk

# Create root window:
root = tk.Tk()

# Create notebook: 
notebook = ttk.Notebook(root)


# Create three frames:
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)

# Create three labels:
ttk.Label(frame1, text="This is Window One").pack(padx=20, pady=50)
ttk.Label(frame2, text="This is Window Two").pack(padx=20, pady=50)
ttk.Label(frame3, text="This is Window Three").pack(padx=20, pady=50)

frame1.pack(fill=tk.BOTH, expand=True)
frame2.pack(fill=tk.BOTH, expand=True)
frame3.pack(fill=tk.BOTH, expand=True)

notebook.add(frame1, text="Window 1")
notebook.add(frame2, text="Window 2")
# notebook.insert("end", frame3, text="Window 3")
notebook.insert(0, frame3, text="Window 3")

notebook.pack(padx=5, pady=5, expand=True)

root.mainloop()


