def menu():
    while True:
        print("1. Cadastrar Aluno")
        print("2. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            print("Cadastrando...")
        elif opcao == "2":
            print("Saindo do programa.")
            #Por que o programa continua rodando e mostrando o menu mesmo digitando 2?    