class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos_internos(arbol):
    if arbol is None:
        return 0
    if arbol.hijos:  # Si el nodo tiene al menos un hijo, es un nodo interno
        contador = 1
    else:
        contador = 0
    for hijo in arbol.hijos:
        contador += contar_nodos_internos(hijo)  # Suma la cantidad de nodos internos en cada subárbol hijo
    return contador

# Ejemplo de uso
# Creamos un árbol de ejemplo
raiz = Nodo(1)
raiz.hijos.append(Nodo(2))
raiz.hijos.append(Nodo(3))
raiz.hijos[0].hijos.append(Nodo(4))
raiz.hijos[0].hijos.append(Nodo(5))
raiz.hijos[1].hijos.append(Nodo(6))

# Contamos los nodos internos en el árbol
cantidad_nodos_internos = contar_nodos_internos(raiz)
print("Cantidad de nodos internos en el árbol:", cantidad_nodos_internos)
