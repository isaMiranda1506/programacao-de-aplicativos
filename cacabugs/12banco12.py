# import sqlite3 

# # O aluno criou a conexão fora das funçõespara "facilitar".
# # Por que isso quebra o sistema quando usamos múltiplos arquivos (módulos)?

# conexao = sqlite3.connect('sistema_escola.db')
# cursor = conexao.cursor()

# def inserir_escola(nome):
#     cursor.execute("INSERT INTO escolas (nome) VALUES (?)" , (nome,))
#     conexao.commit()

# A conexão deve ser criada dentro da função para evitar problemas em projetos com vários módulos.

import sqlite3

def criar_tabela_escolas():
    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')

    conexao.commit()
    conexao.close()

def inserir_escola(nome):
    with sqlite3.connect("sistema_escola.db") as conexao:
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO escolas (nome) VALUES (?)",
            (nome,)
        )

        conexao.commit()

        print("Escola cadastrada com sucesso!")

criar_tabela_escolas()

nome = input("Digite o nome da escola: ")

inserir_escola(nome)