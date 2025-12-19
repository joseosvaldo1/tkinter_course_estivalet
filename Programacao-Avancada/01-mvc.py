# Modelo MVC:

# À medida que a sua aplicação cresce, sua complexidade também aumenta.
# Para tornar a aplicação mais gerenciável, você pode usar o padrão de 
# design Model View Controller (MVC).

# O padrão MVC lhe permite dividir a aplicação em três componentes 
# principais: o modelo, a visão e o controlador. Essa estrutura ajuda 
# você a focar na lógica de cada parte, tornando a aplicação mais fácil 
# de manter, especialmente à medida que ela cresce.

# O modelo no MVC representa os dados. Ele lida com a obtenção ou gravação 
# de dados em um armazenamento, como um banco de dados ou mesmo arquivo.
# Ele também pode conter a lógica para validar os dados, garantindo a 
# integridade deles.

# O modelo não deve depender da visão nem do controlador. Em outras palavras, 
# você pode reutilizar esse modelo em outras aplicações com aplicações web 
# ou móveis.

# O modelo tem uma ligação direta com essa história de que pode ser um banco  
# de dados, um arquivo ou qualquer outra forma de armazenamento dos dados da  
# sua aplicação.

# Já a camada da visão é a interface do usuário que representa os dados no 
# modelo. A visão Ela não se comunica diretamente com o modelo.

# Idealmente, uma visão deve ter muito pouca lógica para receber os dados, 
# ou seja, os dados já devem chegar prontos para sua exibição.

# A visão se comunica diretamente com o controlador. Em aplicações Tkinter, 
# a visão é a janela raiz que contém os widgets.

# Já essa camada do controlador, ela atua como intermediário entre as visões 
# e os modelos. Ela rodeia os dados entre visões e os modelos. Por exemplo, 
# se o usuário clicar no botão Salvar aqui na visão, o controlador rodeia a 
# ação de salvar para o modelo que grava os dados no banco de dados e notifica 
# à visão para exibir uma mensagem de sucesso, por exemplo.



import re
import tkinter as tk
from tkinter import ttk


class Model:
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        """
        Validate the email
        :param value:
        :return:
        """
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

    def save(self):
        """
        Save the email into a file
        :return:
        """
        with open('emails.txt', 'a') as f:
            f.write(self.email + '\n')

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create widgets:

        # Label:
        self.label = ttk.Label(self, text='Email:')
        self.label.grid(row=1, column=0)

        # Email entry:
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=1, column=1, sticky=tk.NSEW)

        # Save button:
        self.save_button = ttk.Button(self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=1, column=3, padx=10)

        # Message:
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=2, column=1, sticky=tk.W)

        # Set the controller:
        self.controller = None

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def save_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.save(self.email_var.get())

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''            


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, email):
        """
        Save the email
        :param email:
        :return:
        """
        try:

            # save the model
            self.model.email = email
            self.model.save()

            # show a success message
            self.view.show_success(f'The email {email} saved!')

        except ValueError as error:
            # show an error message
            self.view.show_error(error)        

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')

        # Create a model
        model = Model('hello@pythontutorial.net')

        # Create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # Create a controller
        controller = Controller(model, view)

        # Set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()            