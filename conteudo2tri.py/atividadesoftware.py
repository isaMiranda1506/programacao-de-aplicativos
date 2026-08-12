def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2




def verificar_situacao(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"




# Testes da função calcular_media
assert calcular_media(8, 6) == 7
assert calcular_media(10, 10) == 10
assert calcular_media(0, 0) == 0


# Testes da função verificar_situacao
assert verificar_situacao(7) == "Aprovado"
assert verificar_situacao(6) == "Aprovado"
assert verificar_situacao(5.9) == "Reprovado"


print("Todos os testes passaram!")

# 1 - mesmo se o aluno não atingir a nota, a mensagem "Todos os testes passaram!" vai ser exibida

# 2 - teste assert verificar_situacao() ==  

# 3 - porque a nota está abaixo da média, então ele confirma quem tiver nota menor que 6

# 4 - teste assert verificar_situacao() == , isso acontece porque a nota passa ser 6, não é maior que 6, então vai retornar reprovado, mas o teste esperava aprovado
