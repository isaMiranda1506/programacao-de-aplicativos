# import sqlite3 

# def cadastrar_escola_manual():
#     # O aluno resolveu gerar o ID por conta própria 
#     id_escola = int(input("Digite o ID para a nova escola: "))
#     nome = input("Nome da escola: ")

#     conexao = sqlite3.connect('sistema_escola.db')
#     cursor = conexao.cursor()

#     # Se rodar duas vezes com o ID 1, o programa fecha abruptamente (Crash).
#     # Aplique a blindagem protetora necessária:
#     cursor.execute("INSERT INTO escolas (id, nome) VALUES (?,?)", (id_escola, nome))

#     conexao.commit()
#     conexao.close()

# O erro ocorre porque o programa tenta inserir um ID que já existe no banco, causando uma violação de chave primária e encerrando a execução - CORREÇÃO



    import sqlite3

def cadastrar_escola_manual():
    id_escola = int(input("Digite o ID para a nova escola: "))
    nome = input("Nome da escola: ")

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    try:
        cursor.execute(
            "INSERT INTO escolas (id, nome) VALUES (?, ?)",
            (id_escola, nome)
        )

        conexao.commit()
        print("Escola cadastrada com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: este ID de escola já está cadastrado!")

    except sqlite3.Error as e:
        print("Erro no banco de dados:", e)

    finally:
        conexao.close()