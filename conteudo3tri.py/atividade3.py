def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)

assert calcular_desconto(100, 0) == 100
assert calcular_desconto(230, 10) == 207
assert calcular_desconto(500, 50) == 250
assert calcular_desconto(1000, 100) == 0
assert calcular_desconto(99.90, 0) == 99.90
