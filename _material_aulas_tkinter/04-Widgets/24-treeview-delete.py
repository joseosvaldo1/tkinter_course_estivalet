import tkinter as tk
from tkinter import ttk

def item_selected(event):
    for selected_item in tree.selection():
        tree.delete(selected_item)


root = tk.Tk()
root.title('Treeview demo')
root.geometry('620x200')

columns = ('first_name', 'last_name', 'email')
tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
tree.heading('first_name', text='First Name')
tree.heading('last_name', text='Last Name')
tree.heading('email', text='Email')

#tree.column('first_name', width=100, anchor=tk.W)
#tree.column('last_name', width=100, anchor=tk.W)
#tree.column('email', width=200, anchor=tk.CENTER)

tree.grid(row=0, column=0, sticky=tk.NSEW)

# adding an item
tree.insert('', tk.END, values=('John', 'Doe', 'john.doe@email.com'))

# insert a the end
tree.insert('', tk.END, values=('Jane', 'Miller', 'jane.miller@email.com'))

# insert at the beginning
tree.insert('', 0, values=('Alice', 'Garcia', 'alice.garcia@email.com'))

tree.bind('<<TreeviewSelect>>', item_selected)

root.mainloop()