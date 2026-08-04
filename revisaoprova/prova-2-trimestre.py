import sqlite3

def cadastrar_hospital():
    conexao = sqlite3.connect('hospital_banco.db')
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS hospitais (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_hospital TEXT NOT NULL,
        cidade TEXT NOT NULL
    )
''')

    try:
        id = int(input("Digite o ID do seu hospital: "))
        nome_hospital = input("Digite o nome do seu hospital: ")
        cidade = input("Digite o nome da cidade: ")

        conexao = sqlite3.connect("hospital_banco.db")
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO hospitais (nome_hospital, cidade) VALUES (?, ?)",
            (nome_hospital, cidade)
        )

        conexao.commit()
        print("Hospital cadastrado.")

    except ValueError:
        print("Erro: o ID do hospital deve ser um número inteiro.")

    except sqlite3.Error:
        print("Erro no banco de dados.")

    finally:
        if conexao:
            conexao.close()

cadastrar_hospital()



def cadastrar_medico():
    conexao = sqlite3.connect('hospital_banco.db')
    cursor = conexao.cursor()


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS medicos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        crm TEXT NOT NULL, 
        id_hospital FOREING KEY hospitais
        )
    ''')


    try:
        id_hospital = int(input("Digite o seu ID: "))
        nome = input("Digite seu nome: ")
        crm = int(input("Digite o seu CRM: "))
       
      
        conexao = sqlite3.connect("hospital_banco.db")
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO medicos (id_hospital, nome, crm) VALUES (?, ?, ?)",
            (id_hospital ,nome, crm)
            )

        conexao.commit()
        print("Médico cadastrado.")

    except ValueError:
        print("Erro: o ID do médico deve ser um número inteiro.")

    except sqlite3.Error:
        print("Erro no banco de dados.")

    finally:
        if conexao:
            conexao.close()

cadastrar_medico()

