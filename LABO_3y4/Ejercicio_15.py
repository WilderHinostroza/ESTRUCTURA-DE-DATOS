import numpy as np

def encontrar_elemento_maximo(matriz):
    # Encontrar el elemento máximo de la matriz utilizando np.max()
    maximo = np.max(matriz)
    return maximo

# Definir una matriz de ejemplo
matriz = np.array([
    [1, 2, 3],
    [4, 9, 6],
    [7, 8, 5]
])

# Llamar a la función para encontrar el elemento máximo
elemento_maximo = encontrar_elemento_maximo(matriz)

# Imprimir el elemento máximo
print("Elemento máximo de la matriz:", elemento_maximo)
