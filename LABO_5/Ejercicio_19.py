def numeros_ordenados_sin_duplicados(conjunto_numeros):
    numeros_ordenados = sorted(conjunto_numeros)
    numeros_sin_duplicados = []
    for numero in numeros_ordenados:
        if numero not in numeros_sin_duplicados:
            numeros_sin_duplicados.append(numero)
    return set(numeros_sin_duplicados)

# Ejemplo de uso
conjunto_numeros = {3, 1, 4, 1, 5, 9, 2, 6, 5}
numeros_ordenados_sin_dupl = numeros_ordenados_sin_duplicados(conjunto_numeros)
print("Números ordenados sin duplicados:", numeros_ordenados_sin_dupl)
