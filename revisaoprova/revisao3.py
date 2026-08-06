import sqlite3

def cadastrar_academia():
    conexao = sqlite3.connect('sistema_academia.db')
    cursor = conexao.cursor()

    

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS academias(
            id INTEGER PRIMARY KEY,
            nome_unidade TEXT NOT NULL,
            bairro TEXT NOT NULL
        )
    ''')

    try:
        id = int(input("Digite o ID da academia: "))
        nome = input("Digite o nome da academia: ")
        bairro = input("Digite o bairro da academia: ")

        conexao = sqlite3.connect("sistema_academia.db")
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO academias (nome_unidade, bairro) VALUES (?, ?)",
            (nome, bairro)
        )

        conexao.commit()
        print("Academia cadastrado!")

    except ValueError:
        print("Erro: o ID da academia deve ser um número inteiro.")

    except sqlite3.Error:
        print("Erro no banco de dados.")

    finally:
        if conexao:
            conexao.close()

cadastrar_academia()           

def cadastrar_alunos():
    conexao = sqlite3.connect('sistema_alunos.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER PRIMARY KEY,
            nome_aluno TEXT NOT NULL,
            mensalidade INTEGER,
            id_alunos INTEGER,
            FOREIGN KEY (id_alunos) REFERENCES academias(id)
        )
    ''')

    cursor.execute("PRAGMA foreign_keys =  ON;")

    try:
        id_alunos = int(input("Digite o ID do aluno: "))
        nome = input("Digite o seu nome: ")
        mensalidade = int(input("Digite a mensalidade da academia: "))

        conexao = sqlite3.connect("sistema_alunos.db")
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO alunos (nome_aluno, mensalidade, id_alunos) VALUES (?, ?, ?)",
            (id_alunos ,nome, mensalidade)
        )

        conexao.commit()
        print("Aluno cadastrado(a)!")

    except ValueError:
        print("Erro: o ID do aluno(a) deve ser um número inteiro.")

    except sqlite3.Error as e:
        print("Erro no banco de dados: ", e)

    finally:
        if conexao:
            conexao.close()
cadastrar_alunos()
    

