# import sqlite3

# def inserir_professor(nome, materia, cpf):
#     try:
#         conexao = sqlite3.connect('siatema-escola.db')
#         cursor = conexao.cursor()
#         # Existe um erro de digitação no comando SQL (INSERTO). 
#         # Por que o programa mostra "CPF já cadastrado" em vez de avisar sobre o erro de sintaxe 
#         cursor.execute("INSERT INTO professores (nome, materia, cpf) VALUES (?,?,?)", (nome, materia, cpf))
#         conexao.commit()
#     execpt sqlite3.Error:
#         print("Erro: Este CPF já está cadastrado no sistema!")   
#     finally: 
#         conexao.close()      

# O erro acontece porque o except sqlite3.Error captura todos os erros do SQLite e mostra a mensagem de CPF duplicado mesmo quando o problema é uma falha de sintaxe ou outro erro - CORREÇÃO 

import sqlite3

def inserir_professor(nome, materia, cpf):
    conexao = None

    try:
        conexao = sqlite3.connect("sistema-escola.db")
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO professores (nome, materia, cpf) VALUES (?,?,?)",
            (nome, materia, cpf)
        )

        conexao.commit()
        print("Professor cadastrado com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: Este CPF já está cadastrado no sistema!")

    except sqlite3.Error as e:
        print("Erro no banco de dados:", e)

    finally:
        if conexao:
            conexao.close()

nome = input("Nome do professor: ")
materia = input("Matéria: ")
cpf = input("CPF: ")

inserir_professor(nome, materia, cpf)