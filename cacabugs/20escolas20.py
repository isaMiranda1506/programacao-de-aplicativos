import sqlite3 

def cadastrar_escola_manual():
    # O aluno resolveu gerar o ID por conta própria 
    id_escola = int(input("Digite o ID para a nova escola: "))
    nome = input("Nome da escola: ")

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # Se rodar duas vezes com o ID 1, o programa fecha abruptamente (Crash).
    # Aplique a blindagem protetora necessária:
    cursor.execute("INSERT INTO escolas (id, nome) VALUES (?,?)", (id_escola, nome))

    conexao.commit()
    conexao.close()