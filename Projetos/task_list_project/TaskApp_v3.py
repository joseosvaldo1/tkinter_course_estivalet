
import tkinter as tk
from tkinter import messagebox, PhotoImage, Toplevel

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")
        self.root.geometry("520x400")
        self.root.configure(bg="#F4F4F4")

        self.tasks = []   # Lista de tarefas (cada item é um dict com 'id', 'frame', 'label', etc.)
        self.next_id = 1  # Contador para IDs únicos

        self.load_images()
        self.create_widgets()
    
    def load_images(self):
        """Carrega as imagens para os botões."""
        # Atenção: os arquivos edit.png e delete.png precisam existir no diretório do script.
        self.edit_icon = PhotoImage(file='edit.png')
        self.delete_icon = PhotoImage(file='delete.png')
    
    def create_widgets(self):
        # Style:
        entry_bg = "#FFFFFF"
        btn_bg = "#4285F4"
        btn_fg = "#FFFFFF"

        # Título centralizado:
        self.title_label = tk.Label(
            self.root,
            text="Lista de tarefas",
            font=("Arial", 16, "bold"),
            bg="#F4F4F4"
        )
        self.title_label.pack(pady=10)
    
        # Frame para a entrada da tarefa:
        self.input_frame = tk.Frame(self.root, bg="#F4F4F4")
        self.input_frame.pack(padx=10, pady=5, fill=tk.X)

        self.task_entry = tk.Entry(
            self.input_frame, 
            width=30, 
            font=("Arial", 12),
            bg=entry_bg
        )
        self.task_entry.pack(
            side=tk.LEFT, 
            padx=5, 
            ipady=5,
            expand=True,
            fill=tk.X
        )

        # Botão para adicionar uma tarefa:
        self.add_button = tk.Button(
            self.input_frame, 
            text="Adicionar Tarefa", 
            command=self.add_task,
            bg=btn_bg,
            fg=btn_fg,
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5
        )
        self.add_button.pack(side=tk.LEFT)

        # Atalho: Enter adiciona tarefa
        self.root.bind("<Return>", lambda e: self.add_task())

        # Frame e canvas para a inserção das tarefas:
        self.task_frame = tk.Frame(self.root, bg="#F4F4F4")
        self.task_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.task_canvas = tk.Canvas(
            self.task_frame,
            bg="#F4F4F4",
            highlightthickness=0
        )
        
        self.task_scrollbar = tk.Scrollbar(
            self.task_frame, 
            orient=tk.VERTICAL,
            command=self.task_canvas.yview
        )
        self.task_list = tk.Frame(self.task_canvas, bg="#F4F4F4")

        # Associando a task_list com a task_scrollbar:
        self.task_list.bind(
            "<Configure>", 
            lambda e: self.task_canvas.configure(
                scrollregion=self.task_canvas.bbox("all")
            )
        )

        self.task_canvas.create_window(
            (0, 0), 
            window=self.task_list, 
            anchor="nw", 
            width=480
        )
        self.task_canvas.configure(yscrollcommand=self.task_scrollbar.set)

        self.task_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.task_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def add_task(self):
        task_text = self.task_entry.get().strip()

        if not task_text:
            messagebox.showerror("Erro", "O campo de tarefa não pode estar vazio!")
            return

        # Gera ID único para a tarefa
        task_id = self.next_id
        self.next_id += 1
    
        task_var = tk.BooleanVar()
        task_frame = tk.Frame(
            self.task_list, 
            bg="#FFFFFF",
            bd=1, 
            relief=tk.RIDGE
        )
        task_frame.pack(fill=tk.X, pady=2)

        # Checkbox (passa o id para o toggle)
        task_checkbox = tk.Checkbutton(
            task_frame,
            variable=task_var,
            command=lambda tid=task_id, lbl=None, var=task_var: self.toggle_task_by_id(tid, var),
            bg="#FFFFFF"
        )
        task_checkbox.pack(side=tk.LEFT, padx=5)

        # Label do texto
        task_label = tk.Label(
            task_frame, 
            text=task_text,
            width=30, 
            anchor="w", 
            font=("Arial", 12)
        )
        task_label.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        # Botão Editar (passa id e label)
        edit_button = tk.Button(
            task_frame,
            image=self.edit_icon,
            command=lambda tid=task_id, lbl=task_label: self.open_edit_window(lbl, tid),
            bd=0, 
            bg="#FFFFFF"
        )
        edit_button.pack(side=tk.LEFT, padx=5)

        # Botão Deletar (passa id e frame)
        delete_button = tk.Button(
            task_frame,
            image=self.delete_icon,
            command=lambda tid=task_id, frm=task_frame: self.delete_task_by_id(tid, frm),
            bd=0,
            bg="#FFFFFF"
        )
        delete_button.pack(side=tk.LEFT, padx=5)

        # Adiciona na lista de tarefas (completo)
        self.tasks.append(
            {
                "id": task_id,
                "frame": task_frame,
                "text": task_text,
                "label": task_label,
                "var": task_var,
                "completed": False
            }
        )

        # Limpa campo e devolve foco
        self.task_entry.delete(0, tk.END)
        self.task_entry.focus_set()
    
    def toggle_task_by_id(self, task_id, var):
        """Marca/desmarca como concluída e atualiza estilo do label."""
        is_done = var.get()

        # Encontrar tarefa pelo ID
        for t in self.tasks:
            if t["id"] == task_id:
                # Atualiza visual
                if is_done:
                    t["label"].config(font=("Arial", 12, "overstrike"), fg="gray")
                else:
                    t["label"].config(font=("Arial", 12), fg="black")
                # Atualiza estado
                t["completed"] = is_done
                break

    def open_edit_window(self, label, task_id):
        """Abre uma janela própria para edição da tarefa."""
        edit_window = Toplevel(self.root)
        edit_window.title("Editar Tarefa")
        edit_window.geometry("300x150")
        edit_window.configure(bg="#F4F4F4")
        edit_window.resizable(False, False)

        tk.Label(
            edit_window,
            text="Edite a Tarefa",
            font=("Arial", 12, "bold"),
            bg="#F4F4F4"
        ).pack(pady=8)

        task_edit_entry = tk.Entry(
            edit_window,
            font=("Arial", 12),
            width=30
        )
        task_edit_entry.insert(0, label.cget("text"))
        task_edit_entry.pack(pady=5)

        button_frame = tk.Frame(edit_window, bg="#F4F4F4")
        button_frame.pack(pady=10)

        save_button = tk.Button(
            button_frame,
            text="Salvar",
            bg="#34A853",
            fg="white",
            font=("Arial", 10),
            command=lambda: self.save_task_edit_by_id(
                task_id, 
                label, 
                task_edit_entry.get(),
                edit_window
            )
        )
        save_button.pack(side=tk.LEFT, padx=5)

        cancel_button = tk.Button(
            button_frame,
            text="Cancelar",
            bg="#EA4335",
            fg="white",
            font=("Arial", 10, "bold"),
            command=edit_window.destroy
        )
        cancel_button.pack(side=tk.LEFT, padx=5)

    def save_task_edit_by_id(self, task_id, label, new_text, edit_window):
        """Salva a edição no label e no registro de self.tasks."""
        new_text = new_text.strip()
        if new_text:
            # Atualiza o label
            label.config(text=new_text)

            # Atualiza o registro na lista
            for t in self.tasks:
                if t["id"] == task_id:
                    t["text"] = new_text
                    break

            edit_window.destroy()
        else:
            messagebox.showerror("Erro", "O campo não pode estar vazio!")

    def delete_task_by_id(self, task_id, frame):
        """Remove o widget e também o registro da tarefa pelo ID."""
        if frame.winfo_exists():
            frame.destroy()

        # Remove da lista pelo ID
        self.tasks = [t for t in self.tasks if t["id"] != task_id]

        # (Opcional) debug:
        print("Tarefas restantes:", [t["text"] for t in self.tasks])


#############################################################################

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
