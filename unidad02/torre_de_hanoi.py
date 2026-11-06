def torres_hanoi(n, origen, auxiliar, destino):
    if n == 1:
        print(f"Mover disco {n} de {origen} a {destino}")
        return
    # Mover los n-1 discos de arriba al auxiliar
    torres_hanoi(n-1, origen, destino, auxiliar)
    # Mover el disco más grande al destino
    print(f"Mover disco {n} de {origen} a {destino}")
    # Mover los n-1 discos del auxiliar al destino
    torres_hanoi(n-1, auxiliar, origen, destino)

# Ejecutar para 3 discos desde A hasta C usando B
torres_hanoi(3, 'A', 'B', 'C')

def hanoi(n,a,b,c):
    if n==1:
        move(a,c)
        return
    hanoi (n-1,a,c,b)
    move(a,c)
    hanoi(n-1,b,a,c)