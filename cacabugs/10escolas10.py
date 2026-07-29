# import sqlite3 

# def deletar_escola_antiga():
#     id_escola = int(input("ID da escola a remover: "))
#     conexao = sqlite3.connect('sistema_escola.db')
#     cursor = conexao.cursor()

#     # Esse comando vai apagar o banco interito se o aluno não prestar atenção.
#     cursor.execute("DELETE FROM escolas WHERE id = id_escola")

#     conexao.commit()
#     conexao.close()
    
# O id_escola é interpretado como o nome de uma coluna, e não como a variável, então deve usar um parâmetro (?) e passar o valor separadamente - CORREÇÃO

import sqlite3

def deletar_escola_antiga():
    id_escola = int(input("ID da escola a remover: "))

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # Remove apenas a escola com o ID informado
    cursor.execute(
        "DELETE FROM escolas WHERE id = ?",
        (id_escola,)
    )

    conexao.commit()
    conexao.close() 