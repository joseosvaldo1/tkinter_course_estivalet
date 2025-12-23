
import tkinter as tk
from tkinter import ttk, messagebox
import requests
import re

# Cores
AZUL_CLARO = "#D0E3F0"
PRETO = "#000000"


def somente_digitos(texto: str) -> str:
    """Remove tudo que não for dígito (útil para CEP com hífen/espacos)."""
    return re.sub(r"\D", "", texto)


class FormularioCEP(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro de Endereço")
        self.geometry("400x420")
        self.configure(bg=AZUL_CLARO)
        self.resizable(False, False)

        self.criar_widgets()

    def criar_widgets(self):
        # Cabeçalho
        lbl_titulo = tk.Label(
            self,
            text="Cadastro de Endereço",
            font=("Arial", 16, "bold"),
            bg=AZUL_CLARO,
            fg=PRETO
        )
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
            ("Estado:", 5, "entry_uf", True),
        ]

        self.entries = {}

        for i, (label, width, var_name, *disabled) in enumerate(campos):
            tk.Label(
                frame,
                text=label,
                font=("Arial", 12, "bold"),
                bg=AZUL_CLARO
            ).grid(row=i, column=0, padx=5, pady=5, sticky="w")

            entry = tk.Entry(frame, width=width, font=("Arial", 12))
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")

            if disabled:
                entry.config(state="disabled")

            self.entries[var_name] = entry

        # Dispara busca ao sair do campo CEP
        self.entries["entry_cep"].bind(
            "<FocusOut>",
            lambda event: self.buscar_cep()
        )

        # Barra de botões
        btns = tk.Frame(self, bg=AZUL_CLARO)
        btns.pack(pady=10)

        btn_salvar = tk.Button(
            btns,
            text="Salvar",
            font=("Arial", 12, "bold"),
            command=self.salvar_dados
        )
        btn_salvar.grid(row=0, column=0, padx=8)

        # NOVO: Botão Limpar
        btn_limpar = tk.Button(
            btns,
            text="Limpar",
            font=("Arial", 12, "bold"),
            command=self.limpar_tudo
        )
        btn_limpar.grid(row=0, column=1, padx=8)

    def buscar_cep(self):
        cep_input = self.entries["entry_cep"].get().strip()
        cep = somente_digitos(cep_input)

        if len(cep) != 8 or not cep.isdigit():
            self.limpar_campos()
            return

        # Endpoint correto do OpenCEP (retorno JSON)
        url = f"https://opencep.com/v1/{cep}.json"
        try:
            response = requests.get(url, timeout=5)
        except requests.RequestException as e:
            self.limpar_campos()
            messagebox.showerror("Erro de conexão", f"Não foi possível consultar o CEP.\n\nDetalhes: {e}")
            return

        if not response.ok:
            self.limpar_campos()
            return

        try:
            dados = response.json()
        except ValueError:
            self.limpar_campos()
            return

        # Trata padrão de erro estilo ViaCEP:
        if isinstance(dados, dict) and dados.get("erro") is True:
            self.limpar_campos()
            return

        # Mapeamento resiliente de chaves
        mapping = {
            "entry_logradouro": ["logradouro", "street", "address", "address_name"],
            "entry_bairro": ["bairro", "district", "neighborhood"],
            "entry_localidade": ["localidade", "cidade", "city"],
            "entry_uf": ["uf", "estado", "state"],
        }

        for campo, possiveis_chaves in mapping.items():
            valor = self._primeiro_valor(dados, possiveis_chaves)
            self._set_entry(campo, valor)

    def _primeiro_valor(self, dados: dict, chaves: list) -> str:
        """Retorna o primeiro valor existente nas chaves fornecidas."""
        for k in chaves:
            v = dados.get(k)
            if v:
                return str(v)
        return ""

    def _set_entry(self, nome: str, valor: str):
        """Define o conteúdo do Entry, habilitando e re-bloqueando se necessário."""
        entry = self.entries[nome]
        was_disabled = (entry["state"] == "disabled")
        if was_disabled:
            entry.config(state="normal")
        entry.delete(0, tk.END)
        entry.insert(0, valor)
        if was_disabled:
            entry.config(state="disabled")

    def limpar_campos(self):
        """Limpa apenas os campos preenchidos pela API (endereço)."""
        for campo in ["entry_logradouro", "entry_bairro", "entry_localidade", "entry_uf"]:
            self._set_entry(campo, "")

    def limpar_tudo(self):
        """Limpa todos os campos do formulário, preservando o estado (habilitado/desabilitado)."""
        # Primeiro limpa os campos de endereço (que ficam bloqueados)
        self.limpar_campos()

        # Limpa os demais campos (CEP, Número, Complemento)
        for campo in ["entry_cep", "entry_numero", "entry_complemento"]:
            entry = self.entries[campo]
            entry.delete(0, tk.END)

    def salvar_dados(self):
        dados = {campo: self.entries[campo].get() for campo in self.entries}
        print("Dados Salvos:", dados)


if __name__ == "__main__":
    app = FormularioCEP()
    app.mainloop()
