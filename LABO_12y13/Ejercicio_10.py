class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def encontrar_minimo(arbol):
    if arbol is None:
        return float('inf')  # Devuelve infinito si el árbol está vacío
    minimo = arbol.valor
    for hijo in arbol.hijos:
        minimo = min(minimo, encontrar_minimo(hijo))  # Actualiza el valor mínimo con el mínimo del subárbol hijo
    return minimo

# Ejemplo de uso
# Creamos un árbol de ejemplo
raiz = Nodo(10)
raiz.hijos.append(Nodo(5))
raiz.hijos.append(Nodo(15))
raiz.hijos[0].hijos.append(Nodo(3))
raiz.hijos[0].hijos.append(Nodo(7))
raiz.hijos[1].hijos.append(Nodo(12))
raiz.hijos[1].hijos.append(Nodo(20))

# Encontramos el nodo con el valor mínimo en el árbol
minimo_valor = encontrar_minimo(raiz)
print("El valor mínimo en el árbol es:", minimo_valor)
