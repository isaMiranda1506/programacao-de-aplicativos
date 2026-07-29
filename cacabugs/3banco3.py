# import sqlite3 

# def criar_tabelas():
#     conexao = sqlite3.connect('sistema_escola.db')
#     cursor = conexao.cursor()

#     # Este bloco quebra ao rodar pela primeira vez em um banco limpo. Por quê? 
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS series (
#             id INTEGER PRIMARY KEY AUTOINCREMENT, 
#             nome_serie TEXT,
#             id_escola INTEGER, 
#             FOREIGN KEY (id_escola) REFERENCES escolas(id)
#         )
#     ''')

#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS escolas (
#             id INTEGER PRIMARY KEY AUTOINCREMENT, 
#             nome TEXT 
#         )
#     ''')
#     conexao.commit()
#     conexao.close()

# O erro é porque, está puxando uma tabela que não existe - CORREÇÃO

import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS escolas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT
            )
        ''')
    
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS series (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_serie TEXT,
                id_escola INTERGER,
                FOREIGN KEY (id_escola)REFERENCES escolas (id)
            )
        ''')
    conexao.commit()
    conexao.close()

    print("Tabelas criadas com sucesso!")

criar_tabelas()