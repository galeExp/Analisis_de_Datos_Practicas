"""Práctica de Laboratorio 2
Ranking de Calificaciones con Ordenamiento Burbuja
Objetivo: Implementar el algoritmo de ordenamiento burbuja (Bubble
Sort) en Python para manipular una lista de 15 calificaciones numéricas
y comprender el impacto de los operadores de comparación en el
ordenamiento ascendente y descendente.
Instrucciones para el alumno:
1. Crea un archivo de Python llamado practica2_burbuja.py.
2. Declara la lista con las 15 calificaciones finales del grupo:
3.Parte 1 (Orden Ascendente):
Escribe el algoritmo de ordenamiento burbuja utilizando una variable
`swapped`
Imprime en pantalla el mensaje `"Orden Ascendente: seguido de la lista
resultante.

4.Parte 2 (Orden Descendente):
Imprime en pantalla el mensaje `"Orden descendente: seguido de la lista
resultante.

Para calificar debes explicar como funciona el método de ordenamiento
Burbuja
"""

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

