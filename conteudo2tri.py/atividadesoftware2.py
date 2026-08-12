def eh_par(numero):
    # retorna True se o número for par e False caso contrário

    return numero % 2 == 0

def calacular_desconto(preco, percentual):
    # retorna o valor final após aplicar o desconto

    return preco - (preco * percentual / 100)

def pode_votar(idade):
    # retorna a situação do voto de acordo com a idade

    if idade < 16:
        return "Não pode votar"
    elif idade < 18 or idade >= 70:
        return "Voto facultativo"
    else:
        return "Voto obrigatório" 

# testes da função eh_par, verifica números pares, ímpares e o caso limite de zero

assert eh_par(8) is True
assert eh_par(7) is False 
assert eh_par(0) is True 

# estes da função calcular_desconto, verifica um desconto comum, um desconto de 0% e um desconto de 100%.

assert calacular_desconto(100, 10) == 90
assert calacular_desconto(200, 0) == 200
assert calacular_desconto(50, 100) == 0

# testes da função pode_votar, verifica idade abaixo do permitido, idade de voto facultativo e idade de voto obrigatório

assert pode_votar(15) == "Não pode votar"
assert pode_votar(16) == "Voto facultativo"
assert pode_votar(18) == "Voto obrigatório"

print("Todos testes passarm!")
