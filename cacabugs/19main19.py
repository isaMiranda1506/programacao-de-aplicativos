# import sqlite3

# def buscar_dados_dinamicos(nome_tabela, id_registro):
#     conexao = sqlite3.connect('sistema_escola.db')
#     cursor = conexao.cursor()

#     # O SQlite joga um erro de sintaxe operacional indicado que não aceita o caractere '?'.
#     # Não podemos parametrizar nomes de tabelas? Como resolver mantendo a segurança?
#     cursor.execute("SELECT * FROM ? WHERE id = ?", (nome_tabela, id_registro))

#     print(cursor.fetchone())
#     conexao.close()

# O erro acontece porque parâmetros (?) do SQLite só podem ser usados para valores, não para nomes de tabelas ou colunas - CORREÇÃO

import sqlite3

def buscar_dados_dinamicos(nome_tabela, id_registro):
    tabelas_permitidas = ["alunos", "professores", "turmas"]

    if nome_tabela not in tabelas_permitidas:
        print("Tabela inválida!")
        return

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute(
        f"SELECT * FROM {nome_tabela} WHERE id = ?",
        (id_registro,)
    )

    print(cursor.fetchone())

    conexao.close()