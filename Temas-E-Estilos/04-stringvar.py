# Stringvar:
# Sintaxe básica: 
# struing_var = tk.StringVar(container, value, name)
# value = '' (string vazia por padrão)
# name => name TCL => PY_VAR1, PY_VAR2, etc.
# name_entry = ttk.Entry(root, textvariable=string_var)

# Para obter o valur da StringVar, utilizamos o método 
# get(): string_var.get()

# Para fazer um monitoramento nas mudanças de valor 
# da StringVar, utilizanos o método trace():
# string_var.trace('w', callback) => 'w' => quando o valor muda
# string_var.trace('r', callback) => 'r' => quando o valor é lido
# string_var.trace('u', callback) => 'w' => quando o valor é apagado

#####################################################################

# Stringvar Entry:

# import tkinter as tk
# from tkinter import ttk


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title('Tkinter StringVar')
#         self.geometry("300x80")

#         self.name_var = tk.StringVar()

#         self.columnconfigure(0, weight=1)
#         self.columnconfigure(1, weight=1)
#         self.columnconfigure(2, weight=1)

#         self.create_widgets()

#     def create_widgets(self):

#         padding = {'padx': 5, 'pady': 5}
        
#         # Label:
#         ttk.Label(self, text='Name:').grid(column=0, row=0, **padding)

#         # Entry:
#         name_entry = ttk.Entry(self, textvariable=self.name_var)
#         name_entry.grid(column=1, row=0, **padding)
#         name_entry.focus()

#         # Button:
#         submit_button = ttk.Button(self, text='Submit', command=self.submit)
#         submit_button.grid(column=2, row=0, **padding)

#         # Output label:
#         self.output_label = ttk.Label(self)
#         self.output_label.grid(column=0, row=1, columnspan=3, **padding)

#     def submit(self):
#         self.output_label.config(text=self.name_var.get())


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


#####################################################################

import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    ERROR = 'Error.TLabel'
    SUCCESS = 'Success.TLabel'
    WARNING = 'Warning.TLabel'

    def __init__(self):
        super().__init__()
        self.title('Change Password')
        self.geometry("300x130")

        self.password_var = tk.StringVar()
        self.confirm_password_var = tk.StringVar()

        # self.confirm_password_var.trace('w', self.validate) 
        self.confirm_password_var.trace_add(['write'], self.validate)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Set style:
        self.style = ttk.Style(self)
        self.style.configure('Error.TLabel', foreground='red')
        self.style.configure('Success.TLabel', foreground='green')
        self.style.configure('Warning.TLabel', foreground='brown')

        self.create_widgets()

    def create_widgets(self):
        """ Create a widget
        """
        padding = {'padx': 5, 'pady': 5, 'sticky': tk.W}

        # Message:
        self.message_label = ttk.Label(self)
        self.message_label.grid(column=0, row=0, columnspan=3, **padding)

        # Password:
        ttk.Label(self, text='New Password:').grid(column=0, row=1, **padding)

        password_entry = ttk.Entry(
            self, 
            textvariable=self.password_var, 
            show='*')
        password_entry.grid(column=1, row=1, **padding)
        password_entry.focus()

        # Confirm password:
        ttk.Label(self, 
                  text='Confirm Password:').grid(column=0, row=2, **padding)

        confirm_password = ttk.Entry(
            self, 
            textvariable=self.confirm_password_var, 
            show='*')
        confirm_password.grid(column=1, row=2, **padding)

        # Change button:
        submit_button = ttk.Button(self, text='Change')
        submit_button.grid(column=0, row=3, **padding)

    def set_message(self, message, type=None):
        """ Set the error or success message.
        """
        self.message_label['text'] = message
        if type:
            self.message_label['style'] = type

    def validate(self, *args):
        """ Validate the password.
        """
        password = self.password_var.get()
        confirm_password = self.confirm_password_var.get()

        if confirm_password == password:
            self.set_message(
                "Success: The new password looks good!", self.SUCCESS)
            return

        if password.startswith(confirm_password):
            self.set_message('Warning: Keep entering the password', 
                             self.WARNING)
            return


        self.set_message("Error: Passwords don't match!", self.ERROR)



if __name__ == "__main__":
    app = App()
    app.mainloop()