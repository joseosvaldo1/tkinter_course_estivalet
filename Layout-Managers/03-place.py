# import tkinter as tk

# root = tk.Tk()
# root.title('Tkinter Place Geometry Manager')
# root.geometry("600x400")

# label1 = tk.Label(master=root, text="Place",bg='red',fg='white')
# # label1.place(x=0,y=0,width=120, height=60)
# # label1.place(x=100,y=200,width=120, height=60)
# # label1.place(x=100,y=200,width=220, height=60)
# # label1.place(relx=0.5,rely=0.5,width=100, height=50)
# label1.place(relx=0.5,rely=0.5,width=100, height=50, anchor=tk.CENTER)


# root.mainloop()



###########################################################################

import tkinter as tk

root = tk.Tk()
root.title('Tkinter place Geometry Manager')

# Label 1:
label1 = tk.Label(
    root,
    text="Absolute placement",
    bg='red',
    fg='white'
)

label1.place(x=20, y=10)

# Label 2
label2 = tk.Label(
    root,
    text="Relative placement",
    bg='blue',
    fg='white'
)

label2.place(relx=0.8, rely=0.2, relwidth=0.5, anchor='ne')

root.mainloop()