import tkinter as tk

root = tk.Tk()
root.title('Tkinter Widget Size')
root.geometry("600x400")

label1 = tk.Label(
    master=root, 
    text="Sizing",
    bg='red',
    fg='white',
    width=8, 
)

label1.pack()

root.mainloop()
