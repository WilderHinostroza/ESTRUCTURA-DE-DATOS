import numpy as np

# Definir una matriz de ejemplo
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Calcular la media de los elementos de la matriz
media = np.mean(matriz)

# Calcular la mediana de los elementos de la matriz
mediana = np.median(matriz)

# Calcular la desviación estándar de los elementos de la matriz
desviacion_estandar = np.std(matriz)

# Imprimir los resultados
print("Media de los elementos de la matriz:", media)
print("Mediana de los elementos de la matriz:", mediana)
print("Desviación estándar de los elementos de la matriz:", desviacion_estandar)
