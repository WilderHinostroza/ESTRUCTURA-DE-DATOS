class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos(arbol):
    if arbol is None:
        return 0
    contador = 1  # Contador para el nodo actual
    for hijo in arbol.hijos:
        contador += contar_nodos(hijo)  # Suma la cantidad de nodos en cada subárbol hijo
    return contador

# Ejemplo de uso
# Creamos un árbol de ejemplo
raiz = Nodo(1)
raiz.hijos.append(Nodo(2))
raiz.hijos.append(Nodo(3))
raiz.hijos[0].hijos.append(Nodo(4))
raiz.hijos[0].hijos.append(Nodo(5))
raiz.hijos[1].hijos.append(Nodo(6))

# Contamos los nodos en el árbol
cantidad_nodos = contar_nodos(raiz)
print("Cantidad de nodos en el árbol:", cantidad_nodos)
