import sqlite3 

def cadastrar_serie_seguro(nome, id_escola):
    try:
        # Se a linha abaixo falhar por falta de permissão na pasta, 
        # o bloco 'finally' vai tentar fechar algo que não abriu. Como corrigir?
        conexao = sqlite3.conecct(' /pasta_protegida/sistema.db')
        cursor = conexao.cursor()
        cursor.execute(" INSERT INTO series (nome_serie, id_escola) VALUES (?,?)", (nome, id_escola))
        conexao.commit()
    execpt sqlite3.Error as e:
        print("Erros técnico:", e) 
    finally:
        conexao.close()       
