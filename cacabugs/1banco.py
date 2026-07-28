# import sqlite3 

# def inicializar_banco():
#     conexao = sqlite3.connect('sistema_escola.db')
#     cursor = conexao.cursor()

#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS escolas (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nome TEXT NOT NULL 
#     )
#     ''')
#     # o banco de dados não está salvando as alterações. Por quê? 
#     conexao.close()

    

    # CORREÇÃO não está salvando, porque falta o  conexao.commit()

    import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS escolas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    ''')

    conexao.commit()
    conexao.close()
