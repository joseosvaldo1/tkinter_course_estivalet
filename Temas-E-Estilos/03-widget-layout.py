# Elementos ttk:
# Layout => style.layout(widget_class)
# Se uma classe de widget não tiver layout, será 
# lançado uma exceção chamada tk.TclError. Caso,
# contrário, será retornada uma tupla com os 
# seguintes itens: (nome_do_elemento, descrição)

# Cada elemento possui uma lista de opções. que 
# especificam sua aparência. Para obter essa lista
# de opções, utilizamos o método element_options:
# style.element_options(nome_do_elemento)

# Para obter uma lista de atributos associadas as 
# opções, temos um outro método, o método lookup():
# do objeto style:
# style.lookup(nome_layout, nome_opcao) 


#####################################################################


# import tkinter as tk
# from tkinter import ttk


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         style = ttk.Style(self)

#         layout = style.layout('TLabel')
#         print(layout)


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# Output: 
# [('Label.border', {'sticky': 'nswe', 'border': '1', 'children': 
# [('Label.padding', {'sticky': 'nswe', 'border': '1', 'children': 
# [('Label.label', {'sticky': 'nswe'})]})]})]


#####################################################################


# import tkinter as tk
# from tkinter import ttk


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         style = ttk.Style(self)

#         # Layout:
#         layout = style.layout('TLabel')
#         print(layout)

#         # Element options:
#         print(style.element_options('Label.border'))
#         print(style.element_options('Label.padding'))
#         print(style.element_options('Label.label'))


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


# Output:: 
# [('Label.border', {'sticky': 'nswe', 'border': '1', 'children': 
# [('Label.padding'[('Label.border', {'sticky': 'nswe', 'border': '1', 
# 'children': [('Label.padding', {'sticky': 'nswe', 'border': '1', 
# 'children': [('Label.label', {'sticky': 'nswe'})]})]})]
# ('relief',)
# [('Label.border', {'sticky': 'nswe', 'border': '1', 'children': 
# [('Label.padding', {'sticky': 'nswe', 'border': '1', 'children': 
# [('Label.label', {'sticky': 'nswe[('Label.border', {'sticky': 'nswe', 
# 'border': '1', 'children': [('Label.padding', {'sticky': 'nswe', 
# 'border': '1', 'children': [('Label.label', {'sticky': 'nswe'})]})]})]

# ('relief',)
# ('padding', 'relief', 'shiftrelief')
# ('compound', 'space', 'text', 'font', 'foreground', 'underline', 
# 'width', 'anchor', 'justify', 'wraplength', 'embossed', 'image', 
# 'stipple', 'background')  

#####################################################################

# import tkinter as tk
# from tkinter import ttk


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         style = ttk.Style(self)

#         # Attributes of the font, foreground, and background
#         # of the Label.label element:
#         print(style.lookup('Label.label', 'font'))
#         print(style.lookup('Label.label', 'foreground'))
#         print(style.lookup('Label.label', 'background'))


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


# Output:
# TkDefaultFont
# SystemWindowText
# SystemButtonFace

#####################################################################


import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('500x100')

        message = 'This is an error message!'

        label = ttk.Label(self, text=message, style='Error.TLabel')
        label.pack(expand=True)

        style = ttk.Style(self)

        style.configure('Error.TLabel', foreground='white')
        style.configure('Error.TLabel', background='red')
        style.configure('Error.TLabel', font=('Helvetica', 12))
        style.configure('Error.TLabel', padding=(10, 10))


if __name__ == "__main__":
    app = App()
    app.mainloop()