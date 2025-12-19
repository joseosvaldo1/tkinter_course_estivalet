import tkinter as tk
from turtle import width

root = tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo - Arc')

canvas = tk.Canvas(root, width=600, height=600, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)

canvas.create_arc((10, 10), (200, 200), style=tk.PIESLICE, width=2)
canvas.create_arc((10, 200), (200, 390), style=tk.CHORD, width=2)
canvas.create_arc((10, 400), (200, 590), style=tk.ARC, width=2)


root.mainloop()