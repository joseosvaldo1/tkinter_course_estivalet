import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        style = ttk.Style(self)

        layout = style.layout('TLabel')
        print(layout)


if __name__ == "__main__":
    app = App()
    app.mainloop()