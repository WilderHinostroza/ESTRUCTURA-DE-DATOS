import numpy as np

# Definir dos matrices de diferentes tamaños
matriz1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

matriz2 = np.array([
    [7, 8],
    [9, 10]
])

# Verificar si las dimensiones de las matrices son compatibles para la suma
if matriz1.shape == matriz2.shape:
    # Sumar las matrices si tienen las mismas dimensiones
    suma_matriz = matriz1 + matriz2
    print("La suma de las matrices es:")
    print(suma_matriz)
else:
    print("No se pueden sumar las matrices porque tienen diferentes dimensiones.")
