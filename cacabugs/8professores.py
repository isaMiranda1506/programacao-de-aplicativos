# import sqlite3

# def cadastrar_professor(nome, cpf):
#     conexao = sqlite3.connect('sistema_escola.db')
#     cursor = conexao.cursor()

#     # O sistema aceita cadastrar dois professores com o mesmo CPF.
#     # Como restringir isso direto na estrutura da tabela abaixo?
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS professores (
#             id INTEGER PRIMARY KEY AUTOINCREMENT, 
#             nome TEXT,
#             cpf TEXT
#         )
#     ''')

# Ele está cadastrando dois professores, para que isso não ocorra, precisa por a palavra UNIQUE na linha do cpf - CORREÇÃO

import sqlite3

def cadastrar_professor(nome, cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # Criar um drop table, para corrigir a tabela ja crada, fiz isso porque criei a primeira tabela sem o cpf, e coloqui ele na segunda vez.
    cursor.execute("""
    DROP TABLE IF EXISTS professores
    """)

    # Cria a tabela novamente com a estrutura correta
    cursor.execute("""
    CREATE TABLE professores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT UNIQUE NOT NULL
    )
    """)

    conexao.commit()

    cursor.execute("""
    INSERT INTO professores (nome, cpf)
    VALUES (?, ?)
    """, ("Gabriel Moya", "99999999999"))

    conexao.commit()

    cursor.execute("SELECT * FROM professores")
    professores = cursor.fetchall()

    print("Lista de Professores:")
    for professor in professores:
        print(professor)

    conexao.close()

cadastrar_professor("Gabriel Moya", "99999999999")  



