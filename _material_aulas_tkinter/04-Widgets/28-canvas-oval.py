import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo - Oval')

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)


points = (
    (50, 150),
    (200, 350),
)
canvas.create_oval(*points, fill='purple')

root.mainloop()