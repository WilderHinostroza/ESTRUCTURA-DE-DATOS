class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]


def ordenar_pila(pila):
    pila_temporal = Pila()
    while not pila.esta_vacia():
        temp = pila.desapilar()
        while not pila_temporal.esta_vacia() and pila_temporal.cima() > temp:
            pila.apilar(pila_temporal.desapilar())
        pila_temporal.apilar(temp)
    return pila_temporal

pila_original = Pila()
elementos = [5, 3, 8, 1, 6]
for elemento in elementos:
    pila_original.apilar(elemento)

pila_ordenada = ordenar_pila(pila_original)

print("Pila original:", elementos)
print("Pila ordenada:", end=" ")
while not pila_ordenada.esta_vacia():
    print(pila_ordenada.desapilar(), end=" ")
