class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def contar_pares_impares(self):
        contador_pares = 0
        contador_impares = 0
        temp = self.cabeza
        while temp:
            if temp.dato % 2 == 0:
                contador_pares += 1
            else:
                contador_impares += 1
            temp = temp.siguiente
        return contador_pares, contador_impares

    def imprimir_adelante(self):
        temp = self.cabeza
        while temp:
            print(temp.dato, end=" - ")
            temp = temp.siguiente
        print("None")

    def imprimir_atras(self):
        temp = self.cola
        while temp:
            print(temp.dato, end=" - ")
            temp = temp.anterior
        print("None")

lista_doble = ListaEnlazadaDoble()
for dato in range(1, 10):
    lista_doble.agregar(dato)

print("Lista hacia adelante:")
lista_doble.imprimir_adelante()

print("\nLista hacia atrás:")
lista_doble.imprimir_atras()

pares, impares = lista_doble.contar_pares_impares()
print("\nNúmero de nodos pares:", pares)
print("Número de nodos impares:", impares)
