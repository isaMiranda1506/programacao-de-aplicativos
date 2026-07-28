import sqlite3 

def verificar_registros():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execut("SELECT * FROM alunos")

    # Por que o segundo print não ostra absolutamente nada no console?
    print("Primeiro print:" , cursor.fetchall())
    print("Segundo print:" , cursor.fetchall())

    conexao.close()