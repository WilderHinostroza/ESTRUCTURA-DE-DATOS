class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def calcular_profundidad_nodo(arbol, valor_nodo, profundidad=0):
    if arbol is None:
        return -1  # Si el árbol está vacío, devuelve -1
    if arbol.valor == valor_nodo:
        return profundidad  # Si encontramos el nodo, devuelve la profundidad actual
    for hijo in arbol.hijos:
        profundidad_hijo = calcular_profundidad_nodo(hijo, valor_nodo, profundidad + 1)
        if profundidad_hijo != -1:  # Si se encontró el nodo en el subárbol hijo
            return profundidad_hijo
    return -1  # Si no se encontró el nodo en ningún subárbol, devuelve -1

# Ejemplo de uso
# Creamos un árbol de ejemplo
raiz = Nodo(1)
raiz.hijos.append(Nodo(2))
raiz.hijos.append(Nodo(3))
raiz.hijos[0].hijos.append(Nodo(4))
raiz.hijos[0].hijos.append(Nodo(5))
raiz.hijos[1].hijos.append(Nodo(6))
raiz.hijos[1].hijos.append(Nodo(7))
raiz.hijos[1].hijos[1].hijos.append(Nodo(8))

# Calculamos la profundidad del nodo con valor 8
valor_nodo = 8
profundidad_nodo = calcular_profundidad_nodo(raiz, valor_nodo)
if profundidad_nodo != -1:
    print(f"La profundidad del nodo con valor {valor_nodo} es: {profundidad_nodo}")
else:
    print(f"No se encontró el nodo con valor {valor_nodo} en el árbol.")
