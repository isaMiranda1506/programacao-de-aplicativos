# import sqlite3

# def listar_alunos_e_turmas():
#     conexao = sqlite3.connect('sistema_escola.db')
#     cursor = conexao.cursor()

#     # O relatório roda, mas repete os dados erroneamente e formato de matriz cruzada
#     # porque falta definir a regra de colagem (vínculo). Conserte o comando SQL:
#     cursor.execute("SELECT alunos.nome, turmas.nome_turma FROM alunos INNER JOIN turmas")

#     for linha in cursor.fetchall():
#         print(f"Aluno: {linha[0]} | Turma: {linha[1]}")
#     conexao.close()    

# O INNER JOIN está sem a cláusula ON, que define como as tabelas se relacionam, sem isso não funciona corretamente - CORREÇÃO

import sqlite3

def listar_alunos_e_turmas():
    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    try:
        cursor.execute('''
            SELECT alunos.nome, turmas.nome_turma
            FROM alunos
            INNER JOIN turmas
            ON alunos.id_turma = turmas.id
        ''')

        alunos = cursor.fetchall()

        if alunos:
            print("\n=== Lista de Alunos e Turmas ===")
            for aluno in alunos:
                print(f"Aluno: {aluno[0]} | Turma: {aluno[1]}")
        else:
            print("Nenhum aluno encontrado.")

    except sqlite3.Error:
        print("Erro ao listar alunos e turmas.")

    finally:
        conexao.close()

listar_alunos_e_turmas()