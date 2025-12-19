import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x150')
        self.resizable(0, 0)
        self.title('Login')

        # UI options:
        paddings = {'padx': 5, 'pady': 5}
        entry_font = {'font': ('Helvetica', 11)}

        # Configure the grid:
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        username = tk.StringVar()
        password = tk.StringVar()

        # Heading:
        heading = ttk.Label(self, text='Member Login', style='Heading.TLabel')
        heading.grid(column=0, row=0, columnspan=2, pady=5, sticky=tk.N)

        # Username:
        username_label = ttk.Label(self, text="Username:")
        username_label.grid(column=0, row=1, sticky=tk.W, **paddings)

        username_entry = ttk.Entry(self, textvariable=username, **entry_font)
        username_entry.grid(column=1, row=1, sticky=tk.E, **paddings)

        # Password:
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(column=0, row=2, sticky=tk.W, **paddings)

        password_entry = ttk.Entry(
            self, textvariable=password, 
            show="*", 
            **entry_font)
        password_entry.grid(column=1, row=2, sticky=tk.E, **paddings)

        # Login button:
        login_button = ttk.Button(self, text="Login")
        login_button.grid(column=1, row=3, sticky=tk.E, **paddings)

        # Configure style:
        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=('Helvetica', 11))
        self.style.configure('TButton', font=('Helvetica', 11))

        # Heading style:
        self.style.configure('Heading.TLabel', font=('Helvetica', 16))


if __name__ == "__main__":
    app = App()
    app.mainloop()