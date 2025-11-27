import tkinter as tk
from tkinter import ttk, messagebox
from utils.utils import aplicar_icone
from database.usuario_dao import UsuarioDAO

class TelaLogin:
    def __init__(self, root, callback_abrir_inicial):
        aplicar_icone(root)
        self.root = root
        self.callback_abrir_inicial = callback_abrir_inicial
        
        self.root.title("Login - HydroLife 💧")
        self.root.geometry("360x400")
        self.root.configure(bg="#e8f4f8")

        self.estilo_ttk()


        tk.Label(
            self.root,
            text="HydroLife",
            font=("Segoe UI", 28, "bold"),
            bg="#e8f4f8",
            fg="#2389da"
        ).pack(pady=15)


        card = tk.Frame(self.root, bg="white", relief="flat")
        card.pack(pady=5, padx=30, fill="x")

        card.configure(highlightbackground="#d0dbe3", highlightthickness=2)
        card.pack_propagate(False)
        card.config(height=200)

        tk.Label(card, text="E-mail:", bg="white", font=("Segoe UI", 11), anchor="w").pack(fill="x", pady=5, padx=20)
        self.entry_email = tk.Entry(card, font=("Segoe UI", 11), relief="solid", bd=1)
        self.entry_email.pack(fill="x", padx=20)

        tk.Label(card, text="Senha:", bg="white", font=("Segoe UI", 11), anchor="w").pack(fill="x", pady=5, padx=20)
        self.entry_senha = tk.Entry(card, show="*", font=("Segoe UI", 11), relief="solid", bd=1)
        self.entry_senha.pack(fill="x", padx=20)

    
        ttk.Button(
            self.root,
            text="Entrar",
            command=self.fazer_login,
            style="RoundedButton.TButton"
        ).pack(pady=15, padx=40, fill="x")

        self.usuario_logado = None


    def estilo_ttk(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "RoundedButton.TButton",
            font=("Segoe UI", 14, "bold"),
            padding=12,
            background="#4fa3f7",
            foreground="white",
            borderwidth=0,
            relief="flat",
        )

        style.map(
            "RoundedButton.TButton",
            background=[("active", "#3c8ed9")]
        )


    def fazer_login(self):
        email = self.entry_email.get().strip()
        senha = self.entry_senha.get().strip()

        if not email or not senha:
            messagebox.showerror("Erro", "Preencha e-mail e senha.")
            return

        usuario = UsuarioDAO.buscar()

        if usuario is None:
            messagebox.showerror(
                "Erro", "Nenhum usuário cadastrado. Faça o cadastro inicial."
            )
            return

        if usuario.email == email and usuario.senha == senha:
            self.usuario_logado = usuario
            
            self.root.destroy()
            self.callback_abrir_inicial(usuario)

        else:
            messagebox.showerror("Erro", "E-mail ou senha incorretos.")
