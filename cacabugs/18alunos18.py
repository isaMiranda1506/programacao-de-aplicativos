# import sqlite3 

# def cadastrar_lista_alunos():
#     lista = [("Ana",1), ("Carlos", 1), ("Beatriz", 2 )]

#     conexao = sqlite3.connect('sistema_escola.db')
#     cursor = conexao.cursor()

#     # O comando executemany quebra com a mensagem: "funcion takes exactly 2 arguments".
#     # Como passar a lista de dados da forma correta dentro dele?
#     cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?,?)", lista)

#     conexao.commit()
#     conexao.close()

# O execute() aceita apenas um conjunto de valores por vez, como lista possui vários registros, é necessário usar executemany(), que foi feito para inserir vários dados em uma única operação - CORREÇÃO


import sqlite3

def cadastrar_lista_alunos():
    lista = [("Ana", 1), ("Carlos", 1), ("Beatriz", 2)]

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.executemany(
        "INSERT INTO alunos (nome, id_turma) VALUES (?, ?)",
        lista
    )

    conexao.commit()
    conexao.close() 

    print("Alunos cadastrados com sucesso!")

cadastrar_lista_alunos()