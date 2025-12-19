from tkinter import Tk, Text

root = Tk()
root.resizable(False, False)
root.title("Text Widget Example")

text = Text(root, height=8)
text.pack()

text.insert('1.0', 'This is a Text widget demo')

print(text.get('1.0','end'))
#print(text.get('1.0','1.5'))

#text['state'] = 'disabled'
#text['state'] = 'normal'


root.mainloop()