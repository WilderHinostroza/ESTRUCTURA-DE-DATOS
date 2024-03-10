class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def calcular_altura_arbol(arbol):
    if arbol is None:
        return 0
    if not arbol.hijos:  # Si el nodo no tiene hijos, su altura es 1
        return 1
    alturas_hijos = [calcular_altura_arbol(hijo) for hijo in arbol.hijos]
    return 1 + max(alturas_hijos)  # La altura del nodo es 1 más la altura máxima de sus hijos

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

# Calculamos la altura del árbol
altura_arbol = calcular_altura_arbol(raiz)
print("Altura del árbol:", altura_arbol)
