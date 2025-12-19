import tkinter as tk

root = tk.Tk()
root.title('Tkinter Window 1')
root.geometry('600x400+50+50')

root2 = tk.Tk()
root2.title('Tkinter Window 2')
root2.geometry('1200x800+50+50')

root2.attributes('-topmost', 1)

# root.lift()
# root.lower()

root.mainloop()
root2.mainloop()