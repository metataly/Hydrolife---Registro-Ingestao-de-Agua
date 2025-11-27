from .conexao import conectar

class IngestaoDAO:

    @staticmethod
    def salvar(usuario_id, quantidade_ml, data_ingestao):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO registro (usuario_id, quantidade_ml, data_ingestao)
        VALUES (?, ?, ?)
        """, (usuario_id, quantidade_ml, data_ingestao))

        conn.commit()
        conn.close()

    @staticmethod
    def buscar_todas(usuario_id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT quantidade_ml, data_ingestao
        FROM registro
        WHERE usuario_id = ?
        ORDER BY data_ingestao
        """, (usuario_id,))

        registros = cursor.fetchall()

        conn.close()

        return [
            {"quantidade_ml": row[0], "data_ingestao": row[1]}
            for row in registros
        ]

    @staticmethod
    def remover_todas(usuario_id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM registro
        WHERE usuario_id = ?
        """, (usuario_id,))

        conn.commit()
        conn.close()
