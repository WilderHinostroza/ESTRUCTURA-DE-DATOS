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

    def eliminar_duplicados(self):
        valores = set()
        temp = self.cabeza
        while temp:
            if temp.dato in valores:
                temp.anterior.siguiente = temp.siguiente
                if temp.siguiente:
                    temp.siguiente.anterior = temp.anterior
                else:
                    self.cola = temp.anterior
            else:
                valores.add(temp.dato)
            temp = temp.siguiente

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
datos = [1, 2, 3, 2, 4, 5, 6, 1, 7, 8, 8]
for dato in datos:
    lista_doble.agregar(dato)

print("Lista original hacia adelante:")
lista_doble.imprimir_adelante()

print("\nLista original hacia atrás:")
lista_doble.imprimir_atras()

lista_doble.eliminar_duplicados()

print("\nLista sin duplicados hacia adelante:")
lista_doble.imprimir_adelante()

print("\nLista sin duplicados hacia atrás:")
lista_doble.imprimir_atras()
