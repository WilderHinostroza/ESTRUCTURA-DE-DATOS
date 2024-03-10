class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaSimple:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            temp = self.cabeza
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo

    def invertir(self):
        previo = None
        actual = self.cabeza
        siguiente = None
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = previo
            previo = actual
            actual = siguiente
        self.cabeza = previo

    def imprimir(self):
        temp = self.cabeza
        while temp:
            print(temp.dato, end=" -> ")
            temp = temp.siguiente
        print("None")

# Ejemplo de uso
lista = ListaEnlazadaSimple()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)
lista.agregar(5)

print("Lista original:")
lista.imprimir()

# Invertir la lista
lista.invertir()

print("\nLista invertida:")
lista.imprimir()
