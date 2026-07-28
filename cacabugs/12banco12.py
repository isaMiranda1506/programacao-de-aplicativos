import sqlite3 

# O aluno criou a conexão fora das funçõespara "facilitar".
# Por que isso quebra o sistema quando usamos múltiplos arquivos (módulos)?

conexao = sqlite3.connect('sistema_escola.db')
cursor = conexao.cursor()

def inserir_escola(nome):
    cursor.execute("INSERT INTO escolas (nome) VALUES (?)" , (nome,))
    conexao.commit()