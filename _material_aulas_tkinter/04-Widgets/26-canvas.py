import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo')

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)

canvas.create_line((50, 50), (100, 100), width=4, fill='red')

root.mainloop()