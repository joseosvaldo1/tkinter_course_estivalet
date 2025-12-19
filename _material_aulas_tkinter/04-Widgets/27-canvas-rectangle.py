import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo - Rectangle')

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)

canvas.create_rectangle((100, 100), (300, 300), fill='green')

root.mainloop()