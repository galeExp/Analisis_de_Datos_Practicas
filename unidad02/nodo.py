class nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
#Creacion de un nodo INDIVIDUAL
nodo_singular=nodo("Primer dato")
print(nodo_singular.dato)
print(nodo_singular.siguiente)

