class Nodo:
    def __init__(self, valor):
        self.dato = valor
        self.siguiente = None

class ListaEnlazadaSimple:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            temp = self.cabeza
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo

    def sumar_nodos(self):
        suma = 0
        temp = self.cabeza
        while temp:
            suma += temp.dato
            temp = temp.siguiente
        return suma

# Ejemplo
lista = ListaEnlazadaSimple()
lista.agregar(11)
lista.agregar(22)
lista.agregar(33)

print("La suma de los nodos es:", lista.sumar_nodos())
