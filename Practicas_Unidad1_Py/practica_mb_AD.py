lista = [5,6,7,8,9,10,9.9,8.8,7.7,6.6,8.1,3.1,9.8,9.9,8.8,]
n= len (lista)
swapped=True
while swapped:
    swapped=False
    for i in range(n-1):
        if lista[i]>lista[i+1]:
            lista[i],lista[i+1]=lista[i+1],lista[i]
            swapped=True
print("Lista ordenada de forma descendente:",lista[::-1])
print("Lista ordenada de forma ascendente:",lista)
