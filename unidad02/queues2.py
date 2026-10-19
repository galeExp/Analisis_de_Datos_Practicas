from collections import deque 
import time 
cola_reproduccion=deque()
#EL USUARIO AGREGA CANCIONES 
cola_reproduccion.append("1.antologia")
cola_reproduccion.append("2.historia de amor")
cola_reproduccion.append("3.aventurero")
#MOSTRAR  LAS CANCIONES EN ESPERA 
print("Canciones en espera:")
for cancion in cola_reproduccion:
    print(" _",cancion)
    print("Inicando reproduccion")
#REPRODUCTOR PROCESA LA COLA CACION 
while cola_reproduccion:
    cancion_actual=cola_reproduccion.popleft()
    print(f"Sonando ahora {cancion_actual}")
time.sleep(1) #simula la duracion del tema 
print(f"Finlizó:{cancion_actual}")
#MUESTRA CUENTAS CANCIONE QUEDAN EN LA COLA
print(f"Quedan {len(cola_reproduccion)} canciones en la cola)")
print("la cola de reproduccion ha terminado")