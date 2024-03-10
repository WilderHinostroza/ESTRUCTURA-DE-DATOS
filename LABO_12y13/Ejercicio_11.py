class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def encontrar_maximo(arbol):
    if arbol is None:
        return float('-inf')  # Devuelve menos infinito si el árbol está vacío
    maximo = arbol.valor
    for hijo in arbol.hijos:
        maximo = max(maximo, encontrar_maximo(hijo))  # Actualiza el valor máximo con el máximo del subárbol hijo
    return maximo

# Ejemplo de uso
# Creamos un árbol de ejemplo
raiz = Nodo(10)
raiz.hijos.append(Nodo(5))
raiz.hijos.append(Nodo(15))
raiz.hijos[0].hijos.append(Nodo(3))
raiz.hijos[0].hijos.append(Nodo(7))
raiz.hijos[1].hijos.append(Nodo(12))
raiz.hijos[1].hijos.append(Nodo(20))

# Encontramos el nodo con el valor máximo en el árbol
maximo_valor = encontrar_maximo(raiz)
print("El valor máximo en el árbol es:", maximo_valor)
