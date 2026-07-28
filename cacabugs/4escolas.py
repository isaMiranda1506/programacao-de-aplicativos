import sqlite3

def cadastrar_escola_rapido():
    nome = input("Digite o nome da escola: ")
    endereco = input("Digite o endereço: ")

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # O código funciona, mas viola uma regra gravíssima de segurança vista em aula.
    cursor.execute(f"INSERT INTO escolas (nome, endereco) VALUES ('{nome}', '{endereco}')")
    conexao.commit()
    conexao.close()