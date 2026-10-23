#Creacion de una matriz 
matriz= [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
#Acceso a elementos de la matriz 
print(matriz[1][2])#Imprimira la fila indice 1 , columna indice 2 
#Modificar Elemento
matriz[0][0]=100
#Recorrer la matriz 
for fila in matriz:
    for elemento in fila:
         print(elemento, end=" ")
    print()
