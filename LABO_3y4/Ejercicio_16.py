import numpy as np

def submatriz_mayor_suma(matriz):
    maxima_suma = -np.inf
    mejor_submatriz = None

    # Iterar sobre todas las submatrices posibles
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            for k in range(i, len(matriz)):
                for l in range(j, len(matriz[0])):
                    suma_actual = np.sum(matriz[i:k+1, j:l+1])
                    # Actualizar si encontramos una suma más grande
                    if suma_actual > maxima_suma:
                        maxima_suma = suma_actual
                        mejor_submatriz = matriz[i:k+1, j:l+1]

    return mejor_submatriz

# Ejemplo de uso
matriz = np.array([
    [1, 2, -1, 4],
    [-2, 0, 3, 2],
    [1, 5, 0, -3],
    [0, 1, 2, 1]
])

submatriz = submatriz_mayor_suma(matriz)
print("Submatriz de mayor suma:")
print(submatriz)
