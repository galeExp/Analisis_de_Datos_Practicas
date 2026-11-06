def potencia(base,exponente):
    if exponenente==0:
        return 1
    else:
        return base*potencia(base,exponente -1)
print(potencia(2,4))