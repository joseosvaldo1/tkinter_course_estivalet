import tkinter as tk

root = tk.Tk()
root.title('Tkinter Place Geometry Manager')
root.geometry("600x400")

label1 = tk.Label(master=root, text="Place",bg='red',fg='white')
label1.place(relx=0.5, rely=0.5, width=100, height=50, anchor=tk.CENTER)

root.mainloop()
