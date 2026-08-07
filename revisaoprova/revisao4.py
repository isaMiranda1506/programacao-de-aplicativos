import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('hotelaria.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")


    try:
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS hoteis (
                id INTEGER PRIMARY KEY,
                nome_hotel TEXT NOT NULL,
                cidade TEXT NOT NULL 
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS quartos (
                id INTEGER PRIMARY KEY,
                numero INTEGER,
                preco_diaria REAL,
                id_hotel INTEGER,
                FOREIGN KEY (id_hotel) REFERENCES hoteis(id)
            )
        ''')
        conexao.commit()

    except ValueError:
        print("Erro: digite apenas números.")
    
    except sqlite3.Error as e:
        print("Erro no banco de dados: ", e)

    finally:
        if conexao:
            conexao.close()

def cadastro_do_hotel():
    conexao = sqlite3.connect('hotelaria.db')
    cursor = conexao.cursor()

    nome = input("Digite o nome do hotel: ")
    cidade = input("Digite o nome da cidade: ")

    cursor.execute(
        "INSERT INTO hoteis (nome_hotel, cidade) VALUES (?, ?)",
        (nome, cidade)
    )

    conexao.commit()
    print("Hotel cadastrado!")
    conexao.close()



def cadastro_do_quarto():
    conexao = sqlite3.connect('hotelaria.db')
    cursor = conexao.cursor()

    numero = int(input("Digite o número do seu quarto: ")) 
    id_hotel = int(input("Digite o ID do hotel: "))
    preco = int(input("Digite o valor da diária: "))   
    
    cursor.execute(
        "INSERT INTO quartos (numero, id_hotel, preco_diaria) VALUES (?, ?, ?)",
        (numero, id_hotel, preco)
    )
    
    conexao.commit()
    print("Quarto cadastrado!")
    conexao.close()

def menu():
    while True:

        inicializar_banco()

        print("\n --- OPÇÕES ---")
        print("1- Cadastrar hotel")
        print("2- Cadastrar quarto")
        print("3- Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastro_do_hotel()

        elif opcao == "2":
            cadastro_do_quarto()

        elif opcao == "3":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")
menu()            

        
