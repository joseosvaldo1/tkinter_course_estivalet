import tkinter as tk

root = tk.Tk()
message = tk.Label(root, text="Hello, World!")
message.pack()
root.mainloop()


# Sintaxe Geral para a criação dos componentes no Tkinter:
# widget = WidgetName(container, **options)