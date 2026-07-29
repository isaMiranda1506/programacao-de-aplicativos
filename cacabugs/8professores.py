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

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT UNIQUE
        )
    ''')

    try:
        cursor.execute('''
            INSERT INTO professores (nome, cpf)
            VALUES (?, ?)
        ''', (nome, cpf))

        conexao.commit()
        print("Professor cadastrado com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: CPF já cadastrado!")

    finally:
        conexao.close()


cadastrar_professor("Gabriel Moya", "99999999999")