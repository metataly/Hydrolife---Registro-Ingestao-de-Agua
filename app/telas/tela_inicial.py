import tkinter as tk
from tkinter import ttk, messagebox
from utils.utils import aplicar_icone

class HydroLifeApp:
    def __init__(self, usuario, registro):
        self.usuario = usuario
        self.registro = registro

        self.root = tk.Tk()
        aplicar_icone(self.root)

        self.root.title("HydroLife")
        self.root.geometry("420x550")
        self.root.configure(bg="#e8f4f8") 

        self.estilo_ttk()
        self.tela_principal()
        self.root.mainloop()


    def estilo_ttk(self):
        style = ttk.Style()
        style.theme_use("clam")

        # Botão 
        style.configure(
            "RoundedButton.TButton",
            font=("Segoe UI", 14, "bold"),
            padding=10,
            background="#4fa3f7",
            foreground="white",
            borderwidth=0,
            relief="flat"
        )

        style.map(
            "RoundedButton.TButton",
            background=[("active", "#3c8ed9")]
        )


    def tela_principal(self):

        tk.Label(
            self.root,
            text="HydroLife",
            font=("Segoe UI", 32, "bold"),
            bg="#e8f4f8",
            fg="#2389da"
        ).pack(pady=20)

        # Card central 
        card = tk.Frame(self.root, bg="white", bd=0, relief="flat")
        card.pack(padx=40, pady=10, fill="both")

        card.configure(highlightbackground="#d0dbe3", highlightthickness=2)
        card.pack_propagate(False)
        card.config(height=480)

        botoes = [
            ("Registrar ingestão", self.tela_registrar),
            ("Resumo do dia", self.mostrar_resumo),
            ("Atualizar dados pessoais", self.tela_atualizar),
            ("Ver meta", self.mostrar_meta),
            ("Mostrar IMC", self.mostrar_imc),
            ("Sair", self.root.quit)
        ]

        for texto, cmd in botoes:
            ttk.Button(
                card,
                text=texto,
                command=cmd,
                style="RoundedButton.TButton"
            ).pack(
                pady=10,
                padx=15,
                fill="x"
            )


    def tela_registrar(self):
        janela = tk.Toplevel(self.root)
        janela.title("Registrar Ingestão")
        janela.geometry("300x170")
        janela.config(bg="#f6fbff")

        tk.Label(janela, text="Quantidade (ml):", font=("Segoe UI", 12), bg="#f6fbff").pack(pady=10)

        entrada = tk.Entry(janela, font=("Segoe UI", 12))
        entrada.pack()

        def salvar():
            try:
                ml = float(entrada.get())
                self.registro.registrar_ingestao(ml)
                messagebox.showinfo("OK", "Ingestão registrada!")
                janela.destroy()
            except ValueError:
                messagebox.showerror("Erro", "Digite um número válido.")

        ttk.Button(janela, text="Registrar", command=salvar, style="RoundedButton.TButton").pack(pady=15)


    def mostrar_resumo(self):
        quanto_falta, porcentagem = self.usuario.exibir_resumo_diario(self.registro)

        janela = tk.Toplevel()
        janela.title("Resumo Diário")
        janela.geometry("300x200")
        janela.config(bg="#f6fbff")

        tk.Label(janela, text="Resumo Diário", font=("Segoe UI", 14, "bold"), bg="#f6fbff").pack(pady=10)
        tk.Label(janela, text=f"Falta beber: {quanto_falta} ml", font=("Segoe UI", 12), bg="#f6fbff").pack(pady=5)
        tk.Label(janela, text=f"Percentual atingido: {porcentagem:.2f}%", font=("Segoe UI", 12), bg="#f6fbff").pack(pady=5)


    def mostrar_meta(self):
        meta = self.usuario.meta_diaria.quantidade_litros
        messagebox.showinfo("Meta diária", f"{meta:.2f} L")


    def mostrar_imc(self):
        imc, status = self.usuario.dados_pessoais.calcular_imc()
        messagebox.showinfo("IMC", f"Seu IMC: {imc:.2f}\n{status}")


    def tela_atualizar(self):
        janela = tk.Toplevel(self.root)
        janela.title("Atualizar Dados")
        janela.geometry("330x500")
        janela.config(bg="#f6fbff")

        campos = {
            "Altura (Exemplo: 1.55)": self.usuario.dados_pessoais.altura,
            "Peso (kg)": self.usuario.dados_pessoais.peso,
            "Idade": self.usuario.dados_pessoais.idade,
            "Sexo (M/F)": self.usuario.dados_pessoais.sexo,
            "Fumante (S/N)": "s" if self.usuario.dados_pessoais.fumante else "n",
            "Atividade física": self.usuario.dados_pessoais.ativ_fisica
        }

        entradas = {}

        for label, valor in campos.items():
            tk.Label(janela, text=label, bg="#f6fbff", font=("Segoe UI", 11)).pack(pady=2)
            e = tk.Entry(janela, font=("Segoe UI", 11))
            e.insert(0, valor)
            e.pack(pady=5)
            entradas[label] = e

        def salvar():
            try:
                nova_altura = float(entradas["Altura (Exemplo: 1.55)"].get())
                novo_peso = float(entradas["Peso (kg)"].get())
                nova_idade = int(entradas["Idade"].get())
                sexo = entradas["Sexo (M/F)"].get()
                fumante = entradas["Fumante (S/N)"].get().lower() == "s"
                ativ = entradas["Atividade física"].get()

                self.usuario.dados_pessoais.atualizar_dados(
                    altura=nova_altura,
                    peso=novo_peso,
                    idade=nova_idade,
                    sexo=sexo,
                    fumante=fumante,
                    ativ_fisica=ativ
                )

                self.usuario.configurar_meta_diaria()

                messagebox.showinfo("OK", "Dados atualizados!")
                janela.destroy()

            except ValueError:
                messagebox.showerror("Erro", "Valores inválidos.")

        ttk.Button(janela, text="Salvar", command=salvar, style="RoundedButton.TButton").pack(pady=15)
