# Progressbar:
# Sintaxe básica:
# ttk.Progressbar(container, orient, length, mode)

# Métodos:
# start([interval]) => Movimenta o indicador da barra de progresso padrão a cada intervalo 
# (intervalo padrão => 50ms).
# step([delta]) => Incrementa o indicador da barra de progresso (por padrão é 1ms)
# stop() => Para a barra de progresso

#######################################################################################

# import tkinter as tk
# from tkinter import ttk

# # Indeterminate Progressbar:

# # Root window:
# root = tk.Tk()
# root.geometry('300x120')
# root.title('Progressbar Demo')

# root.grid()

# # Progressbar:
# pb = ttk.Progressbar(
#     root,
#     orient='horizontal',
#     mode='indeterminate',
#     length=280
# )
# # Place the progressbar:
# pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)


# # Start button:
# start_button = ttk.Button(
#     root,
#     text='Start',
#     command=pb.start
# )
# start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)

# # Stop button:
# stop_button = ttk.Button(
#     root,
#     text='Stop',
#     command=pb.stop
# )
# stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)


# root.mainloop()

#######################################################################################

from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

# Determinate Progressbar:

# Root window:
root = tk.Tk()
root.geometry('300x120')
root.title('Progressbar Demo')


def update_progress_label():
    return f"Current Progress: {pb['value']}%"


def progress():
    if pb['value'] < 100:
        pb['value'] += 20
        value_label['text'] = update_progress_label()
    else:
        showinfo(message='The progress completed!')


def stop():
    pb.stop()
    value_label['text'] = update_progress_label()


# Progressbar:
pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=280
)
# Place the progressbar:
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

# Label:
value_label = ttk.Label(root, text=update_progress_label())
value_label.grid(column=0, row=1, columnspan=2)

# Start button:
start_button = ttk.Button(
    root,
    text='Progress',
    command=progress
)
start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)

stop_button = ttk.Button(
    root,
    text='Stop',
    command=stop
)
stop_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)


root.mainloop()