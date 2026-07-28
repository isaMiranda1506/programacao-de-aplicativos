import sqlite3

def buscar_dados_dinamicos(nome_tabela, id_registro):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # O SQlite joga um erro de sintaxe operacional indicado que não aceita o caractere '?'.
    # Não podemos parametrizar nomes de tabelas? Como resolver mantendo a segurança?
    cursor.execute("SELECT * FROM ? WHERE id = ?", (nome_tabela, id_registro))

    print(cursor.fetchone())
    conexao.close()