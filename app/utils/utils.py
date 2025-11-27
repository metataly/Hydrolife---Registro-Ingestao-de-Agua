import tkinter as tk

def aplicar_icone(janela):
    try:
        icon = tk.PhotoImage(file="assets/water.png")
        janela.iconphoto(True, icon)
        janela._icon_ref = icon 
    except Exception as e:
        print("Erro ao carregar ícone:", e)
