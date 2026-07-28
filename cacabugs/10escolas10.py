import sqlite3 

def deletar_escla_antiga():
    id_escola = int(input("ID da escola a remover: "))
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # Esse comando vai apagar o banco interito se o aluno não prestar atenção.
    cursor.execute("DELETE FROM escolas WHERE id = id_escola")

    conexao.commit()
    conexao.close()
    