historial_navegacion=[]
#OPERACION PARA APILAR (PUSH)
historial_navegacion.append("google.com")
historial_navegacion.append("youtube.com")
historial_navegacion.append("wipedia.com")
print("historial cargado",historial_navegacion )

#OPERACION CIMA (TOP_PEEK)
pagina_actual=historial_navegacion[-1]
print("pagina actual en la pantalla:",pagina_actual)

#OPERACION PARA DESAPILAR(POP)
pagina_cerrada=historial_navegacion[-1]
print("saliendo de :",pagina_cerrada)
print("historial despues de presionar 'Atras'",historial_navegacion)
#OPERACION TANIO(SIZE)
total_paginas=len(historial_navegacion)
print("Paginas guardadas ",total_paginas)
##OPERACION VAVIA (EMPY)
sin_paginas=len(historial_navegacion)==0
print(       )
