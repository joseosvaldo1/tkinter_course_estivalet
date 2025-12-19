# PhotoImage => suporta os seguitnes formatos: GIF, PGM< 
# PPM, PNG, JPG, JPEG, BPM.


import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter PhotoImage Demo')

        # Open the image:
        self.image = Image.open('./assets/python.png')
        self.python_image = ImageTk.PhotoImage(self.image)

        # Display the message in a label:
        ttk.Label(self, image=self.python_image).pack()


if __name__ == '__main__':
    app = App()
    app.mainloop()