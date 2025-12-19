import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo - Image')

canvas = tk.Canvas(root, width=800, height=600, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)

python_image = tk.PhotoImage(file='snake.png')
canvas.create_image(
    (200, 200),
    image=python_image
)


root.mainloop()