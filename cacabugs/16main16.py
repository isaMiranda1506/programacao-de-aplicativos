# def menu():
#     while True:
#         print("1. Cadastrar Aluno")
#         print("2. Sair")
#         opcao = input("Escolha: ")

#         if opcao == "1":
#             print("Cadastrando...")
#         elif opcao == "2":
#             print("Saindo do programa.")
#             #Por que o programa continua rodando e mostrando o menu mesmo digitando 2?    

# O problema é que o while True cria um laço infinito se escolher a opção "2", o programa apenas imprime "Saindo do programa.", mas não há nenhum comando para encerrar o laço, deve se usae break ao selecionar 2 - CORREÇÃO

def menu():
    while True:
        print("1. Cadastrar Aluno")
        print("2. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            print("Cadastrando...")

        elif opcao == "2":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida!")

menu()

