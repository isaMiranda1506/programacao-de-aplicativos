import sqlite3

def cadastrar_cinema():
    conexao = sqlite3.connect('sistema_cinema.db')
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cinema(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_cinema TEXT NOT NULL,
        shopping TEXT NOT NULL
    )
''')
    
    try:
        id = int(input("Digite o ID do cinema: "))
        nome_cinema = input("Digite o nome do cinema: ")
        shopping = input("Digite o nome do shopping: ")

        conexao = sqlite3.connect("sistema_cinema.db")
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO cinema (nome_cinema, shopping) VALUES (?, ?)",
            (nome_cinema, shopping)
        )

        conexao.commit()
        print("Cinema cadastrado!")

    except ValueError:
        print("Erro: o ID do cinema deve ser um número inteiro.")

    except sqlite3.Error:
        print("Erro no banco de dados.")

    finally:
        if conexao:
            conexao.close()

cadastrar_cinema()          

def cadastrar_salas():
    conexao = sqlite3.connect('sistema_salas.db')
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS salas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_sala INTEGER,
        capacidade_de_pessoas INTEGER, 
        id_cinema INTEGER,
        FOREIGN KEY (id_cinema) REFERENCES cinema(id)
    )
''')
    cursor.execute("PRAGMA foreign_keys =  ON;")


    try:
        id = int(input("Digite o ID da sala: "))
        numero = input("Digite o numero da sala: ")
        capacidade = input("Digite a capacidade da sala: ")

        conexao = sqlite3.connect("sistema_salas.db")
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO salas (id_cinema ,numero_sala, capacidade_de_pessoas) VALUES (?, ?, ?)",
            (id, numero, capacidade)
        )

        conexao.commit()
        print("Sala cadastrado!")

    except ValueError:
        print("Erro: o ID da sala deve ser um número inteiro.")

    except sqlite3.Error:
        print("Erro no banco de dados.")

    finally:
        if conexao:
            conexao.close()

cadastrar_salas()

def listar():
    conexao = sqlite3.connect('sistema_salas.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys =  ON;")

    cursor.execute("SELECT * FROM salas")
    dados = cursor.fetchall()
    print(dados)

listar()    



