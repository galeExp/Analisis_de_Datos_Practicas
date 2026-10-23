from collections import deque 
import time
cola_turnos=deque()
cola_turnos.append("Erick Cruz Gonzalez")
cola_turnos.append("Angel Leonardo Lemus Escamilla")
cola_turnos.append("Dulce Marbella Tolentino García")
print("Usuarios en espera:")
for cliente in cola_turnos:
    print(" __",cliente)
    print("Tiempo de espera")
while cola_turnos:
    turno_actual=cola_turnos.popleft()
    time.sleep(1)
    print(f"Turno{turno_actual}")
print(f"Termino el turno{turno_actual}")
print (f"Siguientes turnos {len(cola_turnos)} Clientes en cola")
print("Sin turnos esperando clientes")
