import sqlite3
from database.conexao import conectar
from models.usuario import Usuario
from models.dados_pessoais import DadosPessoais


class UsuarioDAO:

    @staticmethod
    def buscar():
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome, email, senha 
            FROM usuario 
            LIMIT 1
        """)
        row = cursor.fetchone()

        if not row:
            conn.close()
            return None

        id, nome, email, senha = row

        usuario = Usuario(nome, email, senha)
        usuario.id = id

        conn.close()
        return usuario

    @staticmethod
    def salvar(usuario):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO usuario (nome, email, senha)
            VALUES (?, ?, ?)
        """, (usuario.nome, usuario.email, usuario.senha))

        conn.commit()
        usuario_id = cursor.lastrowid
        usuario.id = usuario_id

        conn.close()
        return usuario_id

    @staticmethod
    def atualizar(usuario):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE usuario 
            SET nome=?, email=?, senha=?
            WHERE id=?
        """, (usuario.nome, usuario.email, usuario.senha, usuario.id))

        conn.commit()
        conn.close()
