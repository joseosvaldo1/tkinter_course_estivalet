import tkinter as tk
from tkinter import ttk
import requests



# Cores
AZUL_CLARO = "#D0E3F0"
PRETO = "#000000"



class FormularioCEP(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro de Endereço")
        self.geometry("400x400")
        self.configure(bg=AZUL_CLARO)
        self.resizable(False, False)


        self.criar_widgets()

    def criar_widgets(self):
        # Cabeçalho
        lbl_titulo = tk.Label(
            self, 
            text="Cadastro de Endereço", 
            font=("Arial", 16, "bold"), 
            bg=AZUL_CLARO, fg=PRETO)
        lbl_titulo.pack(pady=10)


        frame = tk.Frame(self, bg=AZUL_CLARO)
        frame.pack(pady=5, padx=10, fill="both", expand=True)

        campos = [
            ("CEP:", 15, "entry_cep"),
            ("Logradouro:", 30, "entry_logradouro", True),
            ("Número:", 10, "entry_numero"),
            ("Complemento:", 20, "entry_complemento"),
            ("Bairro:", 30, "entry_bairro", True),
            ("Cidade:", 30, "entry_localidade", True),
            ("Estado:", 5, "entry_uf", True)
        ]


        self.entries = {}

        for i, (label, width, var_name, *disabled) in enumerate(campos):
            tk.Label(
                frame, 
                text=label, 
                font=("Arial", 12, "bold"), 
                bg=AZUL_CLARO).grid(row=i, column=0, padx=5, pady=5, sticky="w")
            entry = tk.Entry(frame, width=width, font=("Arial", 12))
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")

            if disabled:
                entry.config(state="disabled")
                
            self.entries[var_name] = entry


        self.entries["entry_cep"].bind(
            "<FocusOut>",
            lambda event: self.buscar_cep())


        # Botão Salvar
        btn_salvar = tk.Button(
            self, 
            text="Salvar", 
            font=("Arial", 12, "bold"), 
            command=self.salvar_dados)
        btn_salvar.pack(pady=10)

    def buscar_cep(self):
        cep = self.entries["entry_cep"].get().strip()
        if len(cep) == 8 and cep.isdigit():
            url = f"https://viacep.com.br/ws/{cep}/json/"
            response = requests.get(url)
            if response.status_code == 200:
                dados = response.json()
                if "erro" not in dados:
                    for campo, chave in zip(["entry_logradouro", "entry_bairro", "entry_localidade", "entry_uf"], 
                                            ["logradouro", "bairro", "localidade", "uf"]):
                        self.entries[campo].config(state="normal")
                        self.entries[campo].delete(0, tk.END)
                        self.entries[campo].insert(0, dados.get(chave, ""))
                        self.entries[campo].config(state="disabled")
                else:
                    self.limpar_campos()
            else:
                self.limpar_campos()
        else:
            self.limpar_campos()


    def limpar_campos(self):
        for campo in ["entry_logradouro", 
                "entry_bairro", 
                "entry_localidade", 
                "entry_uf"]:
            self.entries[campo].config(state="normal")
            self.entries[campo].delete(0, tk.END)
            self.entries[campo].config(state="disabled")


    def salvar_dados(self):
        dados = {campo: self.entries[campo].get() for campo in self.entries}
        print("Dados Salvos:", dados)



if __name__ == "__main__":
    app = FormularioCEP()
    app.mainloop()