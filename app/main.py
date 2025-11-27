import tkinter as tk

from database.criar_tabelas import criar_tabelas
from database.usuario_dao import UsuarioDAO
from database.dados_pessoais_dao import DadosPessoaisDAO
from database.meta_diaria_dao import MetaDAO
from database.registro_ingestao_dao import IngestaoDAO

from models.usuario import Usuario
from models.dados_pessoais import DadosPessoais
from models.meta_diaria import MetaDiaria
from models.registro_ingestao import RegistroIngestao

from telas.tela_inicial import HydroLifeApp
from telas.tela_login import TelaLogin
from telas.tela_registro import TelaRegistroInicial

def carregar_usuario_completo(usuario: Usuario):
    dados = DadosPessoaisDAO.buscar(usuario.id)
    meta_litros = MetaDAO.buscar(usuario.id)
    ingestoes = IngestaoDAO.buscar_todas(usuario.id)

    if dados:
        usuario.dados_pessoais = dados

    if meta_litros is not None:
        meta = MetaDiaria()
        meta.quantidade_litros = meta_litros
        usuario.meta_diaria = meta

    registro = RegistroIngestao()
    registro.registros = ingestoes

    return usuario, registro


def abrir_app_principal(usuario):
    usuario_completo, registro = carregar_usuario_completo(usuario)
    HydroLifeApp(usuario_completo, registro)


def main():
    criar_tabelas()

    usuario = UsuarioDAO.buscar()

    if usuario is None:
        root = tk.Tk()
        app_reg = TelaRegistroInicial(root)
        root.mainloop()

        usuario = app_reg.usuario_criado
        if not usuario:
            return

    root_login = tk.Tk()
    app_login = TelaLogin(root_login, abrir_app_principal)
    root_login.mainloop()

    if not app_login.usuario_logado:
        return


if __name__ == "__main__":
    main()
