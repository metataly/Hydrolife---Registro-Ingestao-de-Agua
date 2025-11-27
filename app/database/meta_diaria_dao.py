from database.conexao import conectar

class MetaDAO:

    @staticmethod
    def salvar(usuario_id, quantidade_litros):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO metas (usuario_id, quantidade_litros)
            VALUES (?, ?)
        """, (usuario_id, quantidade_litros))

        conn.commit()
        conn.close()

    @staticmethod
    def buscar(usuario_id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT quantidade_litros FROM metas WHERE usuario_id = ?", (usuario_id,))
        linha = cursor.fetchone()

        conn.close()
        return linha[0] if linha else None
