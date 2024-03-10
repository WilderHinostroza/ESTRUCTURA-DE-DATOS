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

    def buscar(self, valor):
        temp = self.cabeza
        while temp:
            if temp.dato == valor:
                return temp  # Retorna el nodo si se encuentra el valor
            temp = temp.siguiente
        return None  # Retorna None si el valor no se encuentra en la lista

# Ejemplo de uso
lista = ListaEnlazadaSimple()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)

# Buscar un nodo con valor 2 en la lista
nodo_buscado = lista.buscar(2)
if nodo_buscado:
    print("Nodo encontrado con valor:", nodo_buscado.dato)
else:
    print("El valor no se encuentra en la lista.")
