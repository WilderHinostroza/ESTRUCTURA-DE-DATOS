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

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def eliminar_duplicados(self):
        if self.cabeza is None:
            return

        valores_vistos = set()
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.dato in valores_vistos:
                anterior.siguiente = actual.siguiente
            else:
                valores_vistos.add(actual.dato)
                anterior = actual
            actual = actual.siguiente

lista = ListaEnlazadaSimple()
lista.insertar_al_principio(3)
lista.insertar_al_principio(5)
lista.insertar_al_principio(3)
lista.insertar_al_principio(7)
lista.insertar_al_principio(5)

print("Lista original:")
lista.mostrar()

lista.eliminar_duplicados()
