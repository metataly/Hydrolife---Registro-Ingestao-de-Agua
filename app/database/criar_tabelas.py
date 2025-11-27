from .conexao import conectar

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    # Usuário
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT NULL
    );
    """)

    # Dados pessoais
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dados_pessoais (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        altura REAL,
        peso REAL,
        idade INTEGER,
        sexo TEXT,
        fumante INTEGER,
        ativ_fisica TEXT,
        FOREIGN KEY (usuario_id) REFERENCES usuario(id)
    );
    """)

    # Meta diária
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS metas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        quantidade_litros REAL NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuario(id)
    );
    """)

    # Registros de ingestão
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS registro (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        quantidade_ml REAL NOT NULL,
        data_ingestao TEXT NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuario(id)
    );
    """)

    conn.commit()
    conn.close()
