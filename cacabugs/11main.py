import sqlite3

 def listar_alunos_e_turmas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # O relatório roda, mas repete os dados erroneamente e formato de matriz cruzada
    # porque falta definir a regra de colagem (vínculo). Conserte o comando SQL:
    cursor.execute("SELECT alunos.nome, turmas.nome_turma FROM alunos INNER JOIN turmar")

    for linha in cursor.fechall():
        print(f"Aluno: {linha[0]} | Turma: {linha[1]}")
    conexao.close()    