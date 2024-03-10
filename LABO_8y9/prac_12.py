class Nodo:
    def _init_(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaSimple:
    def _init_(self):
        self.cabeza = None

    def insertar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def longitud(self):
        longitud = 0
        actual = self.cabeza
        while actual:
            longitud += 1
            actual = actual.siguiente
        return longitud

lista = ListaEnlazadaSimple()
lista.insertar_al_principio(3)
lista.insertar_al_principio(5)
lista.insertar_al_principio(7)

longitud_lista = lista.longitud()
print("La longitud de la lista enlazada es:",longitud_lista)