def numeros_ordenados_mayor_a_menor(conjunto_numeros):
    return sorted(conjunto_numeros, reverse=True)

# Ejemplo de uso
conjunto_numeros = {3, 1, 4, 1, 5, 9, 2, 6, 5}
numeros_ordenados_conjunto = numeros_ordenados_mayor_a_menor(conjunto_numeros)
print("Números ordenados de mayor a menor:", numeros_ordenados_conjunto)
