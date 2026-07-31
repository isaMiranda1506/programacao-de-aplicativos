# import sqlite3 

# def verificar_registros():
#     conexao = sqlite3.connect('sistema_escola.db')
#     cursor = conexao.cursor()

#     cursor.execute("SELECT * FROM alunos")

#     # Por que o segundo print não ostra absolutamente nada no console?
#     print("Primeiro print:" , cursor.fetchall())
#     print("Segundo print:" , cursor.fetchall())

#     conexao.close()

# O fetchall recebe todos os dados de uma vez só, na segunda chamada não tem nada porque ele fica vazio - CORREÇÃO

import sqlite3

def verificar_registros():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    registros = cursor.fetchall()

    print("Primeiro print:", registros)
    print("Segundo print:", registros)

    conexao.close()

verificar_registros()