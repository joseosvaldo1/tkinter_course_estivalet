# Agendar ação com o método after():
# Todos os widgets tem o método after() no tkinter. A sintaxe deste 
# método é: widget.after(delay, callback=None). Esse método after 
# chama a função de callback uma vez após um certo atraso em ms 
# dentro do loop principal do Tkinter. Então a gente especifica um delay.
# Após esse delay ter finalizado e chamado o callback, se você não 
# fornecer esse callback, o método after vai se comportar como a função 
# time.sleep() do Python normal em ms.

########################################################################


# import tkinter as tk
# from tkinter import ttk
# import time

# Using time.sleep():

# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title('Tkinter after() Demo')
#         self.geometry('300x100')

#         self.style = ttk.Style(self)

#         self.button = ttk.Button(self, text='Wait 3 seconds')
#         self.button['command'] = self.start
#         self.button.pack(expand=True, ipadx=10, ipady=5)

#     def start(self):
#         self.change_button_color('red')
#         time.sleep(3)     
#         self.change_button_color('black')



#     def change_button_color(self, color):
#         self.style.configure('TButton', foreground=color)
#         print(color)


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()



########################################################################



# import tkinter as tk
# from tkinter import ttk
# import time

# Using after():


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title('Tkinter after() Demo')
#         self.geometry('300x100')

#         self.style = ttk.Style(self)

#         self.button = ttk.Button(self, text='Wait 3 seconds')
#         self.button['command'] = self.start
#         self.button.pack(expand=True, ipadx=10, ipady=5)

#     def start(self):
#         self.change_button_color('red')
#         self.after(3000,lambda: self.change_button_color('black'))


#     def change_button_color(self, color):
#         self.style.configure('TButton', foreground=color)
#         print(color)


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


########################################################################

# Digital clock:

import tkinter as tk
from tkinter import ttk
import time


class DigitalClock(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure the root window:
        self.title('Digital Clock')
        self.resizable(0, 0)
        self.geometry('250x80')
        self['bg'] = 'black'

        # Change the background color to black:
        self.style = ttk.Style(self)
        self.style.configure(
            'TLabel',
            background='black',
            foreground='red')

        # Label:
        self.label = ttk.Label(
            self,
            text=self.time_string(),
            font=('Digital-7', 40))

        self.label.pack(expand=True)

        # Schedule an update every 1 second
        self.label.after(1000, self.update)

    def time_string(self):
        return time.strftime('%H:%M:%S')

    def update(self):
        """ Update the label every 1 second."""

        self.label.configure(text=self.time_string())

        # Schedule another timer:
        self.label.after(1000, self.update)


if __name__ == "__main__":
    clock = DigitalClock()
    clock.mainloop()