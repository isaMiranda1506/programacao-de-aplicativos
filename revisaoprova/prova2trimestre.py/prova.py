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
        return "FastFood cadastrado!"

    except ValueError:
        print("Erro: o faturamento deve ser apenas números.")    
        
    except sqlite3.Error as e:
        print("Erro no banco de dados.", e)
    finally:
        if conexao:
            conexao.close()           

def cadastrar_restaurante(id_rede, cidade):
    conexao = sqlite3.connect('sistema_fastfood.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")


    try:
        
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
        return "Restaurante cadastrado!"

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
        return "Dados listados"

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
        return "Dados listados"
        

    except sqlite3.Error as e:
        print("Erro no banco de dados.", e)
    finally:
        if conexao:
            conexao.close()    


def atualizar_fastfood(id, nome, faturamento):
    conexao = sqlite3.connect('sistema_fastfood.db')
    cursor = conexao.cursor()

    try:
        
        cursor.execute("""

            UPDATE redes_fast_food
            SET nome_franquia = ?, faturamento_anual = ? 
            WHERE id = ?
        """, (nome, faturamento, id)   
        )
        conexao.commit()
        return "Fastfood atualizado com sucesso!"

    except ValueError:
        print("Erro: o ID da franquia deve ser um número inteiro.")
    except sqlite3.Error as e:
        print("Erro no banco de dados.", e)
    finally:
        if conexao:
            conexao.close()     



def atualizar_restaurante(id, unidade):
    conexao = sqlite3.connect('sistema_fastfood.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            UPDATE restaurantes
            SET cidade_unidade = ?
            WHERE id = ?
        """, (unidade, id)    
        )
        conexao.commit()
        return "Restaurante atualizado com sucesso!"

    except ValueError:
        print("Erro: o ID do restaurante deve ser um número inteiro.")
    except sqlite3.Error as e:
        print("Erro no banco de dados.", e)
    finally:
        if conexao:
            conexao.close()        

def excluir_fastfood(id):
    conexao = sqlite3.connect('sistema_fastfood.db')
    cursor = conexao.cursor()

    try:
        
        cursor.execute("""
            
            DELETE FROM redes_fast_food
            WHERE id = ? 
        """, (id,)
        )
        conexao.commit()
        return "Fastfood excluído com sucesso!"
        
    except ValueError:
        print("Erro: o ID da franquia deve ser um número inteiro.")
    except sqlite3.Error as e:
        print("Erro no banco de dados.")
    finally:
        if conexao:
            conexao.close()        
    
def excluir_restaurante(id):
    conexao = sqlite3.connect('sistema_fastfood.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("""

            DELETE FROM restaurantes
            WHERE id = ?
        """, (id,)    
        )
        conexao.commit()
        return "Restaurante excluído com sucesso! "  
        
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
                id_rede = int(input("Digite o ID da franquia: "))
                cidade = input("Digite a cidade/unidade do restaurante: ")
                cadastrar_restaurante(id_rede,cidade)
            elif opcao == "3":
                listar_fastfood()
            elif opcao == "4":
                listar_restaurante()
            elif opcao == "5":
                id = int(input("Digite o ID que deseja atualizar: "))
                nome = input("Digite um novo nome, para atualizar: ")
                faturamento = float(input("Digite um novo faturamento, para atualizar: "))
                atualizar_fastfood(id, nome, faturamento)
            elif opcao == "6":
                id = int(input("Digite o ID que deseja atualizar: "))
                unidade = input("Digite o nome da unidade que desejea atualizar: ")
                atualizar_restaurante()
            elif opcao == "7":
                id = int(input("Digite o ID que deseja excluir: "))
                excluir_fastfood()
            elif opcao == "8":
                id = int(input("Digite o ID que deseja excluir: "))
                excluir_restaurante()
            elif opcao == "9":
                print("Programa encerrado.")
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Erro: digite apenas números.")        
#menu()             

assert cadastrar_fastfood() == "FastFood cadastrado!"
assert cadastrar_restaurante(1, "Paranavaí") == "Restaurante cadastrado!"
assert listar_fastfood() == "Dados listados"
assert listar_restaurante() == "Dados listados"
assert atualizar_fastfood(1, "KFC", 23.000000) == "Fastfood atualizado com sucesso!"
assert atualizar_restaurante(1, "LAUER") == "Restaurante atualizado com sucesso!"
assert excluir_fastfood(1) == "Fastfood excluído com sucesso!"
assert excluir_restaurante(1) == "Restaurante excluído com sucesso! "

print("Todos os teste passaram com sucesso!")







