# import tkinter as tk

# root = tk.Tk()
# root.title('Tkinter Widget Size')
# root.geometry("600x400")

# label1 = tk.Label(
#     master=root, 
#     text="Sizing",
#     bg='red',
#     fg='white',
#     width=8, 
# )

# label1.pack()

# root.mainloop()


#############################################################

# import tkinter as tk

# root = tk.Tk()
# root.title('Tkinter Widget Size')
# root.geometry("600x400")

# label1 = tk.Label(
#     master=root, 
#     text="Sizing",
#     bg='red',
#     fg='white',
#     width=8, 
#     font=('Helvetica', 24)
# )

# label1.pack()

# root.mainloop()


#############################################################

import tkinter as tk

root = tk.Tk()
root.title('Tkinter Widget Size')
root.geometry("600x400")

label1 = tk.Label(
    master=root, 
    text="Sizing", 
    bg='red', 
    fg='white', 
    width=20
)
label1.pack(
    # Remova o fill e execute o programa para ver o efeito
    # fill='x' 
)

root.mainloop()

