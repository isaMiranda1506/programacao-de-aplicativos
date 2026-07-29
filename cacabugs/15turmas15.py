# import sqlite3

# def criar_tabela_turma():
#     conexao = sqlite3.connect('sistema_escola.db')
#     cursor = conexao.cursor()

#     # O SQlite acusa erro de sintaxe próximo ao FOREIGN KEY. Cadê  o erro?
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS turmas (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             nome_turma TEXT,
#             id_serie
#             FOREIGN KEY (id_serie) REFERENCES series(id)
#         )
#     ''')
# conexao.commit()
# conexao.close()

#A coluna id_serie está sem o tipo de dado INTEGER, falta uma vírgula após a definição da coluna id_serie.conexao.commit() e conexao.close() devem estar dentro da função - CORREÇÃO

import sqlite3

def criar_tabela_turma():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_turma TEXT,
            id_serie INTEGER,
            FOREIGN KEY (id_serie) REFERENCES series(id)
        )
    ''')

    conexao.commit()
    conexao.close()