# Treeview:
# Sintaxe básica:
# tree = ttk.Treeview(container, **options)

###########################################################

# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo


# # Treeview Tabular:

# # Create root window:
# root = tk.Tk()
# root.title('Treeview Demo')
# root.geometry('620x200')

# # Define columns:
# columns = ('first_name', 'last_name', 'email')

# tree = ttk.Treeview(root, columns=columns, show='headings')

# # Define headings:
# tree.heading('first_name', text='First Name')
# tree.heading('last_name', text='Last Name')
# tree.heading('email', text='Email')

# # Generate sample data:
# contacts = []
# for n in range(1, 100):
#     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

# # Add data to the treeview:
# for contact in contacts:
#     tree.insert('', tk.END, values=contact)


# def item_selected(event):
#     for selected_item in tree.selection():
#         item = tree.item(selected_item)
#         record = item['values']
#         # Show a message:
#         showinfo(title='Information', message=','.join(record))


# tree.bind('<<TreeviewSelect>>', item_selected)

# tree.grid(row=0, column=0, sticky='nsew')

# # Add a scrollbar:
# scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
# tree.configure(yscroll=scrollbar.set)
# scrollbar.grid(row=0, column=1, sticky='ns')

# # Run the app:
# root.mainloop()

###########################################################


# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.title('Treeview demo')
# root.geometry('620x200')

# columns = ('first_name', 'last_name', 'email')
# tree = ttk.Treeview(root, columns=columns, show='headings')

# # define headings
# tree.heading('first_name', text='First Name')
# tree.heading('last_name', text='Last Name')
# tree.heading('email', text='Email')

# tree.grid(row=0, column=0, sticky=tk.NSEW)

# # adding an item
# tree.insert('', tk.END, values=('John', 'Doe', 'john.doe@email.com'))

# # insert a the end
# tree.insert('', tk.END, values=('Jane', 'Miller', 'jane.miller@email.com'))

# # insert at the beginning
# tree.insert('', 0, values=('Alice', 'Garcia', 'alice.garcia@email.com'))

# root.mainloop()


###########################################################


import tkinter as tk
from tkinter import ttk

def item_selected(event):
    for selected_item in tree.selection():
        tree.delete(selected_item)

# Create root window:
root = tk.Tk()
root.title('Treeview Demo')
root.geometry('620x200')

columns = ('first_name', 'last_name', 'email')
tree = ttk.Treeview(root, columns=columns, show='headings')

# Define headings:
tree.heading('first_name', text='First Name')
tree.heading('last_name', text='Last Name')
tree.heading('email', text='Email')

#tree.column('first_name', width=100, anchor=tk.W)
#tree.column('last_name', width=100, anchor=tk.W)
#tree.column('email', width=200, anchor=tk.CENTER)

tree.grid(row=0, column=0, sticky=tk.NSEW)

# Adding an item:
tree.insert('', tk.END, values=('John', 'Doe', 'john.doe@email.com'))

# Insert a the end:
tree.insert('', tk.END, values=('Jane', 'Miller', 'jane.miller@email.com'))

# Insert at the beginning:
tree.insert('', 0, values=('Alice', 'Garcia', 'alice.garcia@email.com'))

tree.bind('<<TreeviewSelect>>', item_selected)

root.mainloop()


###########################################################