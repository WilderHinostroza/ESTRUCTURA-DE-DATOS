import numpy as np

def matriz_covarianza(matriz1, matriz2):
    # Calcular la matriz de covarianza entre las dos matrices
    covarianza = np.cov(matriz1, matriz2)
    return covarianza

# Ejemplo de uso
matriz1 = np.array([[1, 2, 3], [4, 5, 6]])
matriz2 = np.array([[7, 8, 9], [10, 11, 12]])

covarianza = matriz_covarianza(matriz1, matriz2)
print("Matriz de covarianza:")
print(covarianza)
