import sqlite3
from models.dados_pessoais import DadosPessoais
from database.conexao import conectar

class DadosPessoaisDAO:

    @staticmethod
    def buscar(usuario_id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT altura, peso, idade, sexo, fumante, ativ_fisica
            FROM dados_pessoais
            WHERE usuario_id=?
        """, (usuario_id,))

        row = cursor.fetchone()
        conn.close()

        if not row:
            return None

        altura, peso, idade, sexo, fumante, ativ_fisica = row

        return DadosPessoais(altura, peso, idade, sexo, fumante, ativ_fisica)

    @staticmethod
    def salvar(usuario_id, dados):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO dados_pessoais 
            (usuario_id, altura, peso, idade, sexo, fumante, ativ_fisica)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            usuario_id,
            dados.altura,
            dados.peso,
            dados.idade,
            dados.sexo,
            dados.fumante,
            dados.ativ_fisica
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def atualizar(usuario_id, dados):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE dados_pessoais
            SET altura=?, peso=?, idade=?, sexo=?, fumante=?, ativ_fisica=?
            WHERE usuario_id=?
        """, (
            dados.altura,
            dados.peso,
            dados.idade,
            dados.sexo,
            dados.fumante,
            dados.ativ_fisica,
            usuario_id
        ))

        conn.commit()
        conn.close()
