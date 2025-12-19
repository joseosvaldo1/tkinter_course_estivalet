
# Listbox:
# Sintaxe básica:
# listbox = tk.Listbox(container, listvariable, height)
# selectmode => opção para indicar a forma de seleção dos itens => browse (padrão) 
# e extended.
# curseselection() => Retorna a lista dos índices que foram selecionados
# ListboxSelect => Quando os elementos da lista mudam.


# ################################################################################

# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo

# # Create the root window:
# root = tk.Tk()
# root.geometry('200x100')
# root.resizable(False, False)
# root.title('Listbox')

# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# # Create a list box:
# langs = ['Java', 'C#', 'C', 'C++', 'Python',
#         'Go', 'JavaScript', 'PHP', 'Swift']

# langs_var = tk.StringVar(value=langs)

# listbox = tk.Listbox(
#     root,
#     listvariable=langs_var,
#     height=6,
#     selectmode='extended')

# listbox.grid(
#     column=0,
#     row=0,
#     sticky='nwes'
# )

# # handle event
# def items_selected(event):
#     """ Handle item selected event.
#     """
#     # Get selected indices:
#     selected_indices = listbox.curselection()
#     # Get selected items: 
#     selected_langs = ",".join([listbox.get(i) for i in selected_indices])
#     msg = f'You selected: {selected_langs}'

#     showinfo(
#         title='Information',
#         message=msg)


# listbox.bind('<<ListboxSelect>>', items_selected)

# root.mainloop()

################################################################################

################################################################################

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Create the root window:
root = tk.Tk()
root.geometry('200x100')
root.resizable(False, False)
root.title('Listbox')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create a list box:
langs = ('Java', 'C#', 'C', 'C++', 'Python',
        'Go', 'JavaScript', 'PHP', 'Swift')

langs_var = tk.StringVar(value=langs)

listbox = tk.Listbox(
    root,
    listvariable=langs_var,
    height=6,
    selectmode='extended')

listbox.grid(
    column=0,
    row=0,
    sticky='nwes'
)

# Link a scrollbar to a list
scrollbar = ttk.Scrollbar(
    root,
    orient='vertical',
    command=listbox.yview
)

listbox['yscrollcommand'] = scrollbar.set

scrollbar.grid(
    column=1,
    row=0,
    sticky='ns')

# Handle event:
def items_selected(event):
    """ Handle item selected event
    """
    # Get selected indices:
    selected_indices = listbox.curselection()
    # Get selected items:
    selected_langs = ",".join([listbox.get(i) for i in selected_indices])
    msg = f'You selected: {selected_langs}'

    showinfo(
        title='Information',
        message=msg)


listbox.bind('<<ListboxSelect>>', items_selected)

root.mainloop()