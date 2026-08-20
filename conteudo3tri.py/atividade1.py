def eh_par(numero):
    if numero %2 == 0:
        return True
    else:
        return False    

assert eh_par(4) == True
assert eh_par(5) == False
assert eh_par(0) == True
assert eh_par(-6) == True