import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        style = ttk.Style(self)

        # attributes of the font, foreground, and background
        # of the Label.label element
        print(style.lookup('Label.label', 'font'))
        print(style.lookup('Label.label', 'foreground'))
        print(style.lookup('Label.label', 'background'))


if __name__ == "__main__":
    app = App()
    app.mainloop()