def promedio ():
    calificaciones=[10,10,10,10,8,5]
    suma=0
    for i in calificaciones:
        suma +=i
    promedio=suma/len(calificaciones)
    return promedio    
resultado=promedio()
print("Tu promedio es:",resultado)


def datos_laborales(nombre,edad,nss,rfc,sexo):
    print(f"""
    Nombre: {nombre}
    Edad: {edad}
    NSS: {nss}
    RFC: {rfc}
    Sexo: {sexo}
    """)
datos_laborales("Elena Carrillo",28,"123456789","CACJ880101","No definido")