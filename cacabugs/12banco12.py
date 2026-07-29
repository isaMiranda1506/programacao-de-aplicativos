# import sqlite3 

# # O aluno criou a conexão fora das funçõespara "facilitar".
# # Por que isso quebra o sistema quando usamos múltiplos arquivos (módulos)?

# conexao = sqlite3.connect('sistema_escola.db')
# cursor = conexao.cursor()

# def inserir_escola(nome):
#     cursor.execute("INSERT INTO escolas (nome) VALUES (?)" , (nome,))
#     conexao.commit()

# A conexão deve ser criada dentro da função para evitar problemas em projetos com vários módulos.

import sqlite3

def inserir_escola(nome):
    with sqlite3.connect("sistema_escola.db") as conexao:
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO escolas (nome) VALUES (?)",
            (nome,)
        )
        conexao.commit()