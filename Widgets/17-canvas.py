# Canvas:
# Sintaxe básica:
# canvas = tk.Canvas(container, **options)

# Methods:
# Line -> create_line()
# Rectangle => create_rectangle()
# Oval => create_oval()
# Arc => create_arc()
# Polygon => create_polygon()
# Text => create_text()
# Image => Create_image()

###########################################################

# import tkinter as tk

# root = tk.Tk()
# root.geometry('800x600')
# root.title('Canvas Demo')

# canvas = tk.Canvas(root, width=600, height=400, bg='white')
# canvas.pack(anchor=tk.CENTER, expand=True)


# root.mainloop()


###########################################################


import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo')

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)

# Create a line:
# canvas.create_line((50, 50), (100, 100), width=4, fill='red')

# Create a rectangle:
# canvas.create_rectangle((100, 100), (300, 300), fill='green')

# Create an oval:
# points = ((50, 150), (200, 350))
# canvas.create_oval(*points, fill='purple')


# Create a polygon:
# points = ((100, 300), (200, 200), (300,300))
# canvas.create_polygon(*points, fill='blue')

# Create text:
# canvas.create_text(
#     (300, 100), 
#     text="Canvas Demo",
#     fill='orange',
#     font='tkDefaultFont 24'

# )


# Create a arc:
# canvas.create_arc((10, 10), (200, 200), style=tk.PIESLICE, width=2)
# canvas.create_arc((10, 200), (200, 390), style=tk.CHORD, width=2)
# canvas.create_arc((10, 400), (200, 590), style=tk.ARC, width=2)

# Create an image:
# python_image = tk.PhotoImage(file='snake.png')
# canvas.create_image(
#     (300, 200),
#     image=python_image
# )


# Binding an event:
python_image = tk.PhotoImage(file='snake.png')
image_item = canvas.create_image(
    (300, 200),
    image=python_image
)

canvas.tag_bind(
    image_item,
    '<Button-1>',
    lambda e: canvas.delete(image_item)
)



root.mainloop()


###########################################################

