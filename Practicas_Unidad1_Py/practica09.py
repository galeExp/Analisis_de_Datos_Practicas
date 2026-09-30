def escuela_cabrona():
    print("""
    Que es el amor definamos amor ....
    
    """)
    escuela_cabrona()

def nota_min():
    return(6.0)


def rendimiento(cal):
    if cal <7:
         print ("Reprobado")
    elif  7 <= cal <= 9.4:
        print("Aprobado")
    elif  9.5 <= cal <= 10:
        print("Excelente")
rendimiento(6)

def promedio(examen,tareas):
    return examen*.3 + tareas*.7
print(promedio(10,9))




