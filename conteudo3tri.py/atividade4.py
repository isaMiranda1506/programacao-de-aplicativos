def pode_entrar(idade, acompanhado):
    if idade >= 18 or acompanhado:
        return True
    return False

assert pode_entrar(19, desacompanhado) == True
assert pode_entrar(16, acompanhado) == True
assert pode_entrar(15, desacompanhado) == False
assert pode_entrar(18) == True
assert pode_entrar(17, acompanhado) == True
 
