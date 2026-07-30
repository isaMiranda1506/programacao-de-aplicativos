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

def criar_tabela_turmas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            id_serie INTEGER,
            id_prof INTEGER,
            FOREIGN KEY (id_serie) REFERENCES series(id),
            FOREIGN KEY (id_prof) REFERENCES professores(id)
        )
    ''')

    conexao.commit()
    conexao.close()

def cadastrar_professores():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()    

    cursor.execute(
        "INSERT INTO professores(nome, id_serie) VALUES (?, ?)",
        (nome, id_serie)
    )

    conexao.commit()
    print("Professor cadastrado com sucesso!")

def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    try:
        cursor.execute('''
            INSERT INTO turmas (nome, id_serie, id_prof)
            VALUES (?, ?, ?)
        ''', (nome, id_serie, id_prof))

        conexao.commit()
        print("Turma cadastrada com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: professor ou série não existe.")

    finally:
        conexao.close()

criar_tabela_turmas()

cadastrar_turma("Turma A", 1, 1)