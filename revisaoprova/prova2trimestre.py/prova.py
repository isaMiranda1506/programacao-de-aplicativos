import sqlite3

def sistema_fast_food():
    conexao = sqlite3.connect('sistema_fastfood.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    try:       
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS redes_fast_food (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_franquia TEXT NOT NULL,
            faturamento_anual REAL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS restaurantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cidade_unidade TEXT NOT NULL, 
            id_rede INTEGER,
            FOREIGN KEY (id_rede) REFERENCES redes_fast_food(id)
            )
        ''')
        conexao.commit()

    except ValueError:
        print("Erro: digite apenas números.")

    except sqlite3.Error as e:
        print("Erro no banco de dados.", e)
    finally:
        if conexao:
            conexao.close()

def cadastrar_fastfood():
    conexao = sqlite3.connect('sistema_fastfood.db')
    cursor = conexao.cursor()

    try:
        nome = input("Digite o nome da franquia: ")
        faturamento = float(input("Digite o faturamento da franquia: "))

        cursor.execute(
            "INSERT INTO redes_fast_food (nome_franquia, faturamento_anual) VALUES (?, ?)",
            (nome, faturamento)
        )  

        conexao.commit()
        print("FastFood cadastrado!")

    except ValueError:
        print("Erro: o faturamento deve ser apenas números.")    
        
    except sqlite3.Error as e:
        print("Erro no banco de dados.", e)
    finally:
        if conexao:
            conexao.close()           

def cadastrar_restaurante():
    conexao = sqlite3.connect('sistema_fastfood.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")


    try:
        id_rede = int(input("Digite o ID da franquia: "))
        cidade = input("Digite a cidade/unidade do restaurante: ")

        cursor.execute(
            "SELECT id FROM redes_fast_food WHERE id = ?",
            (id_rede,)
        )

        rede = cursor.fetchone()

        if rede is None:
            print("Erro: esse fastfood não existe.")
            return

        cursor.execute(
            "INSERT INTO restaurantes (id_rede, cidade_unidade) VALUES (?, ?)",
            (id_rede, cidade)
        )
        
        conexao.commit()
        print("Restaurante cadastrado!")

    except ValueError:
        print("Erro: o ID da franquia deve ser um número inteiro.")

    except sqlite3.Error as e:
        print("Erro no banco de dados.", e)
    finally:
        if conexao:
            conexao.close()

        
def listar_fastfood():
    conexao = sqlite3.connect('sistema_fastfood.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    try:
        cursor.execute("SELECT * FROM redes_fast_food")
        dados = cursor.fetchall()
        print(dados)

    except sqlite3.Error as e:
        print("Erro no banco de dados.", e)
    finally:
        if conexao:
            conexao.close()



def listar_restaurante():
    conexao = sqlite3.connect('sistema_fastfood.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    try:
        cursor.execute("SELECT * FROM restaurantes")
        dados = cursor.fetchall()
        print(dados)
        

    except sqlite3.Error as e:
        print("Erro no banco de dados.", e)
    finally:
        if conexao:
            conexao.close()    


def atualizar_fastfood():
    conexao = sqlite3.connect('sistema_fastfood.db')
    cursor = conexao.cursor()

    try:
        id = int(input("Digite o ID que deseja atualizar: "))
        nome = input("Digite um novo nome, para atualizar: ")
        faturamento = float(input("Digite um novo faturamento, para atualizar: "))

        cursor.execute("""

            UPDATE redes_fast_food
            SET nome_franquia = ?, faturamento_anual = ? 
            WHERE id = ?
        """, (nome, faturamento, id)   
        )
        conexao.commit()
        print("Fastfood atualizado com sucesso!")

    except ValueError:
        print("Erro: o ID da franquia deve ser um número inteiro.")
    except sqlite3.Error as e:
        print("Erro no banco de dados.", e)
    finally:
        if conexao:
            conexao.close()     



def atualizar_restaurante():
    conexao = sqlite3.connect('sistema_fastfood.db')
    cursor = conexao.cursor()

    try:
        id = int(input("Digite o ID que deseja atualizar: "))
        unidade = input("Digite o nome da unidade que desejea atualizar: ")

        cursor.execute("""
            UPDATE restaurantes
            SET cidade_unidade = ?
            WHERE id = ?
        """, (unidade, id)    
        )
        conexao.commit()
        print("Restaurante atualizado com sucesso!")

    except ValueError:
        print("Erro: o ID do restaurante deve ser um número inteiro.")
    except sqlite3.Error as e:
        print("Erro no banco de dados.", e)
    finally:
        if conexao:
            conexao.close()        

def excluir_fastfood():
    conexao = sqlite3.connect('sistema_fastfood.db')
    cursor = conexao.cursor()

    try:
        id = int(input("Digite o ID que deseja excluir: "))

        cursor.execute("""
            
            DELETE FROM redes_fast_food
            WHERE id = ? 
        """, (id,)
        )
        conexao.commit()
        print("Fastfood excluído com sucesso!")
        
    except ValueError:
        print("Erro: o ID da franquia deve ser um número inteiro.")
    except sqlite3.Error as e:
        print("Erro no banco de dados.")
    finally:
        if conexao:
            conexao.close()        
    
def excluir_restaurante():
    conexao = sqlite3.connect('sistema_fastfood.db')
    cursor = conexao.cursor()

    try:
        id = int(input("Digite o ID que deseja excluir: "))

        cursor.execute("""

            DELETE FROM restaurantes
            WHERE id = ?
        """, (id,)    
        )
        conexao.commit()
        print("Restaurante excluído com sucesso! ")    
        
    except ValueError:
        print("Erro: o ID do restaurante deve ser um número inteiro.")
    except sqlite3.Error as e:
        print("Erro no banco de dados.", e) 
    finally:
        if conexao:
            conexao.close()

def menu():
    sistema_fast_food()

    while True:
        try:            
            print("\n ---- OPÇÕES ----")
            print("1 - Cadastrar fastfood")
            print("2 - Cadastrar restaurante")
            print("3 - Listar fastfood")
            print("4 - Listar restaurante")
            print("5 - Atualizar fastfood")
            print("6 - Atualizar restaurante")
            print("7 - Excluir fastfood")
            print("8 - Excluir restaurante")
            print("9 - Sair")

            opcao = input("Escolha uma opção: ")                     
        
            if opcao == "1":
                cadastrar_fastfood()
            elif opcao == "2":
                cadastrar_restaurante()
            elif opcao == "3":
                listar_fastfood()
            elif opcao == "4":
                listar_restaurante()
            elif opcao == "5":
                atualizar_fastfood()
            elif opcao == "6":
                atualizar_restaurante()
            elif opcao == "7":
                excluir_fastfood()
            elif opcao == "8":
                excluir_restaurante()
            elif opcao == "9":
                print("Programa encerrado.")
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Erro: digite apenas números.")        
menu()             






