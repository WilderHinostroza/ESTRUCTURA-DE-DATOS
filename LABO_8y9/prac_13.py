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

    def concatenar(self, otra_lista):
        if not self.cabeza:
            self.cabeza = otra_lista.cabeza
        else:
            temp = self.cabeza
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = otra_lista.cabeza

    def imprimir(self):
        temp = self.cabeza
        while temp:
            print(temp.dato, end=" -> ")
            temp = temp.siguiente
        print("None")

# Ejemplo de uso
lista1 = ListaEnlazadaSimple()
lista1.agregar(1)
lista1.agregar(2)
lista1.agregar(3)

lista2 = ListaEnlazadaSimple()
lista2.agregar(4)
lista2.agregar(5)
lista2.agregar(6)

print("Lista 1:")
lista1.imprimir()

print("\nLista 2:")
lista2.imprimir()

# Concatenar las listas
lista1.concatenar(lista2)

print("\nDespués de concatenar:")
lista1.imprimir()
