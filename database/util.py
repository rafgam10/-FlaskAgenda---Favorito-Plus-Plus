import sqlite3

DB_CAMINHO = "Banco.db"
#DB_CAMINHO = "agenda.db"    

def conectar():
    return sqlite3.connect(DB_CAMINHO)


def Lista_contatos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Contatos;")
    linhas = cursor.fetchall()
    conn.close()
    
    contatos = []
    
    for linha in linhas:
        contato = {
            "id": linha[0],
            "nome": linha[1],
            "telefone": linha[2],
            "email": linha[3],
            "favorito": linha[4]
        }
        contatos.append(contato)
    return contatos

def Add_contato(nome:str, telefone:str, email:str, favorito:int):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO Contatos (nome, telefone, email, favorito)
        VALUES (?, ?, ?, ?)
        """,
        (nome, telefone, email, int(favorito))
    )
    conn.commit()
    conn.close()
    return

def Editar_contato(id:int, nome:str, telefone:str, email:str, favorito:int):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute(
    """
        UPDATE Contatos
        SET nome = ?, telefone = ?, email = ?, favorito = ?
        WHERE id = ?;
    """, (nome, telefone, email, favorito, id)
    )
    
    conn.commit()
    conn.close()
    return

def Deletar_contato(id:int):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM Contatos WHERE id = ?",(int(id),))
    
    conn.commit()
    conn.close()
    return

def Lista_Favoritos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Contatos WHERE favorito = 1;")
    linhas = cursor.fetchall()
    conn.close()
    
    contatos = []
    
    for linha in linhas:
        contato = {
            "id": linha[0],
            "nome": linha[1],
            "telefone": linha[2],
            "email": linha[3],
            "favorito": linha[4]
        }
        contatos.append(contato)
    return contatos
    
    return contatos
