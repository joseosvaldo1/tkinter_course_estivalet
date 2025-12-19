import tkinter as tk

root = tk.Tk()
root.title('Tkinter Place Geometry Manager')
root.geometry("600x400")

label1 = tk.Label(master=root, text="Place",bg='red',fg='white')
label1.place(x=0,y=0,width=120, height=60)

root.mainloop()