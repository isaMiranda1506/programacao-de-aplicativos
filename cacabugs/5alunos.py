# import sqlite3

# def vincular_aluno_turma():
#     nome = input("Nome do aluno: ")
#     # Se o usuário digitar "Turma B" em vez do número do ID, o sistema quebra.
#     # O try/execpt abaixo falhou em capturar esse erro. Qual o problema?
#     try:
#         id_turma = int(input("Digite o ID numérico da turma: "))

#         conexao = sqlite3.connect('sistema_escola.db')
#         cursor = conexao.cursor()
#         cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?,?)", (nome, id_turma))
#         conexao.commit()
#     except sqlite3.Error:
#         print("Erro no banco de dados!")
#     finally:
#         conexao.close()    

# Conversão feita por int() que gera ValueError. Falta um execept para capturar o erro de escrita - CORREÇÃO

import sqlite3

def vincular_aluno_turma():
    conexao = None

    try:
        nome = input("Nome do aluno: ")
        id_turma = int(input("Digite o ID numérico da turma: "))

        conexao = sqlite3.connect("sistema_escola.db")
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO alunos (nome, id_turma) VALUES (?, ?)",
            (nome, id_turma)
        )

        conexao.commit()
        print("Aluno cadastrado com sucesso!")

    except ValueError:
        print("Erro: o ID da turma deve ser um número inteiro.")

    except sqlite3.Error:
        print("Erro no banco de dados.")

    finally:
        if conexao:
            conexao.close()
vincular_aluno_turma()

