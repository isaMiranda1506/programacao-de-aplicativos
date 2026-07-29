# import sqlite3 

# def cadastrar_serie_seguro(nome, id_escola):
#     try:
#         # Se a linha abaixo falhar por falta de permissão na pasta, 
#         # o bloco 'finally' vai tentar fechar algo que não abriu. Como corrigir?
#         conexao = sqlite3.conecct(' /pasta_protegida/sistema.db')
#         cursor = conexao.cursor()
#         cursor.execute(" INSERT INTO series (nome_serie, id_escola) VALUES (?,?)", (nome, id_escola))
#         conexao.commit()
#     execpt sqlite3.Error as e:
#         print("Erros técnico:", e) 
#     finally:
#         conexao.close()       

# Se a conexão falhar na 7, a variável conexao nunca será criada, com isso o finally tenta fechar algo que não foi criado - CORREÇÃO

import sqlite3

def cadastrar_serie_seguro(nome, id_escola):
    conexao = None

    try:
        conexao = sqlite3.connect('/pasta_protegida/sistema.db')
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)",
            (nome, id_escola)
        )

        conexao.commit()

    except sqlite3.Error as e:
        print("Erro técnico:", e)

    finally:
        if conexao is not None:
            conexao.close()
