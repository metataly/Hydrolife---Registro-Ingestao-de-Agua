import tkinter as tk
from tkinter import ttk, messagebox
from utils.utils import aplicar_icone

from database.usuario_dao import UsuarioDAO
from database.dados_pessoais_dao import DadosPessoaisDAO
from database.meta_diaria_dao import MetaDAO
from models.usuario import Usuario
from models.dados_pessoais import DadosPessoais
from models.meta_diaria import MetaDiaria


class TelaRegistroInicial:
    def __init__(self, root):
        aplicar_icone(root)
        self.root = root
        self.root.title("Cadastro - HydroLife 💧")
        self.root.geometry("380x600")
        self.root.configure(bg="#e8f4f8")

        self._estilo_ttk()

    
        tk.Label(
            self.root,
            text="Cadastro 💧",
            font=("Segoe UI", 26, "bold"),
            bg="#e8f4f8",
            fg="#2389da"
        ).pack(pady=10)


        container = tk.Frame(self.root, bg="#e8f4f8")
        container.pack(fill="both", expand=True, padx=10, pady=0)

        canvas = tk.Canvas(
            container,
            bg="#e8f4f8",
            highlightthickness=0,
            borderwidth=0
        )
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        self.frame = tk.Frame(canvas, bg="white")
        card = canvas.create_window((0, 0), window=self.frame, anchor="nw")

        def ajustar_largura(event):
            canvas.itemconfig(card, width=event.width)

        canvas.bind("<Configure>", ajustar_largura)
        self.frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))


        self._titulo_secao("Informações de Login")
        self._criar_campo("Nome completo", "nome")
        self._criar_campo("E-mail", "email")
        self._criar_campo("Senha", "senha", show="*")

        self._titulo_secao("Dados Pessoais")
        self._criar_campo("Altura (ex: 1.55)", "altura")
        self._criar_campo("Peso (kg)", "peso")
        self._criar_campo("Idade", "idade")
        self._criar_campo("Sexo (M/F)", "sexo")
        self._criar_campo("Fumante (S/N)", "fumante")
        self._criar_campo("Atividade física (leve/moderado/intenso)", "ativ_fisica")


        ttk.Button(
            self.root,
            text="Cadastrar",
            style="RoundedButton.TButton",
            command=self.cadastrar
        ).pack(pady=12, padx=40, fill="x")

        self.usuario_criado = None
        self.registro_ingestao = None


    def _estilo_ttk(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "RoundedButton.TButton",
            font=("Segoe UI", 14, "bold"),
            padding=12,
            background="#4fa3f7",
            foreground="white",
            relief="flat",
            borderwidth=0
        )

        style.map(
            "RoundedButton.TButton",
            background=[("active", "#3a8bd4")]
        )


    def _titulo_secao(self, texto):
        tk.Label(
            self.frame,
            text=texto,
            bg="white",
            fg="#2389da",
            font=("Segoe UI", 13, "bold"),
            anchor="w"
        ).pack(fill="x", pady=(18, 5), padx=20)


    def _criar_campo(self, rotulo, chave, show=None):
        tk.Label(
            self.frame,
            text=f"{rotulo}:",
            bg="white",
            fg="#444",
            font=("Segoe UI", 11),
            anchor="w"
        ).pack(fill="x", padx=20)

        entry = tk.Entry(
            self.frame,
            font=("Segoe UI", 11),
            show=show,
            relief="solid",
            bd=1
        )
        entry.pack(fill="x", pady=5, padx=20)

        setattr(self, f"entry_{chave}", entry)


    def cadastrar(self):
        try:
            nome = self.entry_nome.get().strip()
            email = self.entry_email.get().strip()
            senha = self.entry_senha.get().strip()

            if not nome or not email or not senha:
                messagebox.showerror("Erro", "Nome, e-mail e senha são obrigatórios.")
                return

            altura = float(self.entry_altura.get().replace(",", "."))
            peso = float(self.entry_peso.get().replace(",", "."))
            idade = int(self.entry_idade.get())
            sexo = self.entry_sexo.get().strip().upper()
            fumante = self.entry_fumante.get().strip().lower() == "s"
            ativ_fisica = self.entry_ativ_fisica.get().strip().lower()

            usuario = Usuario(nome, email, senha)
            usuario_id = UsuarioDAO.salvar(usuario)

            dados = DadosPessoais(altura, peso, idade, sexo, fumante, ativ_fisica)
            usuario.dados_pessoais = dados
            DadosPessoaisDAO.salvar(usuario_id, dados)

            meta = MetaDiaria()
            meta.calcular_meta(peso=peso, fumante=fumante, ativ_fisica=ativ_fisica)

            usuario.meta_diaria = meta
            MetaDAO.salvar(usuario_id, meta.quantidade_litros)

            self.usuario_criado = usuario

            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            self.root.destroy()

        except ValueError:
            messagebox.showerror("Erro", "Verifique os valores numéricos digitados.")
