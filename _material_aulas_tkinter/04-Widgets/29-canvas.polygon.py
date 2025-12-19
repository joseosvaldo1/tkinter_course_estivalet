import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo - Polygon')

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)


# create a polygon
points = (
    (100, 300),
    (200, 200),
    (300, 300),
)
canvas.create_polygon(*points, fill='blue')

root.mainloop()