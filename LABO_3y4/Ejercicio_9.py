import numpy as np

# Definir una matriz de ejemplo
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Calcular las coordenadas del elemento central
fila_central = matriz.shape[0] // 2
columna_central = matriz.shape[1] // 2

# Acceder al elemento central de la matriz
elemento_central = matriz[fila_central, columna_central]

# Imprimir el elemento central
print("Elemento central de la matriz:", elemento_central)
