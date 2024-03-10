class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos_hoja(arbol):
    if arbol is None:
        return 0
    if not arbol.hijos:  # Si el nodo no tiene hijos, es una hoja
        return 1
    contador = 0
    for hijo in arbol.hijos:
        contador += contar_nodos_hoja(hijo)  # Suma la cantidad de nodos hoja en cada subárbol hijo
    return contador

# Ejemplo de uso
# Creamos un árbol de ejemplo
raiz = Nodo(1)
raiz.hijos.append(Nodo(2))
raiz.hijos.append(Nodo(3))
raiz.hijos[0].hijos.append(Nodo(4))
raiz.hijos[0].hijos.append(Nodo(5))
raiz.hijos[1].hijos.append(Nodo(6))

# Contamos los nodos hoja en el árbol
cantidad_nodos_hoja = contar_nodos_hoja(raiz)
print("Cantidad de nodos hoja en el árbol:", cantidad_nodos_hoja)
