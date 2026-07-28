# import sqlite3

# def cadastrar_turma(nome, id_serie, id_prof):
#     conexao = sqlite3.connect('sistema_escola.db')
#     cursor = conexao.cursor()
#     cursor.execute("PRAGMA foreign_keys = ON; ")

#     # Se o id_prof não existir, ocorre um IntegrityError.
#     # Se o erro acontecer, o que ocorre com a liha conexao.close()?
#     cursor.execute('''
#         CREAT TABLE IF NOT EXIXTS professores (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             nome TEXT,
#             cpf TEXT
#         )
#     ''')

# Ela não sera executada se o erro acontecer, porque o código não possui try,except e finally, mas se houver o erro o commit e o close não será executado - CORREÇÃO

import sqlite3

def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute('''
            INSERT INTO turmas (nome, id_serie, id_prof)
            VALUES (?, ?, ?)
        ''', (nome, id_serie, id_prof))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: professor ou série não existe.")
    finally:
        conexao.close()
