# Text:
# Sintaxe básica:
# text = tk.Text(master, conf={}, **kw)  kw => keywords

########################################################################


# from tkinter import Tk, Text

# root = Tk()
# root.resizable(False, False)
# root.title("Text Widget Example")

# text = Text(root, height=8)
# text.pack()


# root.mainloop()


########################################################################

# from tkinter import Tk, Text

# root = Tk()
# root.resizable(False, False)
# root.title("Text Widget Example")

# text = Text(root, height=8)
# text.pack()

# text.insert('1.0', 'This is a Text widget demo.')


# root.mainloop()


########################################################################

# from tkinter import Tk, Text

# root = Tk()
# root.resizable(False, False)
# root.title("Text Widget Example")

# text = Text(root, height=8)
# text.pack()

# text.insert('1.0', 'This is a Text widget demo.')
# text_content = text.get('1.0', 'end')
# print(text_content)


# root.mainloop()

########################################################################

from tkinter import Tk, Text

root = Tk()
root.resizable(False, False)
root.title("Text Widget Example")

text = Text(root, height=8)
text.pack()

text.insert('1.0', 'This is a Text widget demo.')

# text['state'] = 'disabled'
# text['state'] = 'normal'  (padrão)


root.mainloop()

