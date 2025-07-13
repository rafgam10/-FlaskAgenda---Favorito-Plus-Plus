import sqlite3

# Caminho do banco
DB_CAMINHO = "agenda.db"

# Conectar ao banco (cria o arquivo se não existir)
conn = sqlite3.connect(DB_CAMINHO)
cursor = conn.cursor()

# Criar tabela de contatos
cursor.execute("""
CREATE TABLE IF NOT EXISTS Contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT,
    favorito INTEGER DEFAULT 0
)
""")

# Inserir dados de exemplo
contatos_exemplo = [
    ("João da Silva", "9999-1234", "joao@email.com", 1),
    ("Maria Oliveira", "8888-5678", "maria@email.com", 0),
    ("Carlos Lima", "7777-0000", "carlos@email.com", 1)
]

cursor.executemany("""
INSERT INTO Contatos (nome, telefone, email, favorito)
VALUES (?, ?, ?, ?)
""", contatos_exemplo)

# Salvar e fechar
conn.commit()
conn.close()

print("Banco criado e populado com sucesso!")
