def numeros_divisibles(conjunto_numeros, divisor):
    numeros_divisibles = set()
    for numero in conjunto_numeros:
        if numero % divisor == 0:
            numeros_divisibles.add(numero)
    return numeros_divisibles

# Ejemplo de uso
conjunto_numeros = {2, 3, 4, 5, 6, 7, 8, 9, 10}
divisor = 3
numeros_divisibles_por_3 = numeros_divisibles(conjunto_numeros, divisor)
print("Números divisibles por", divisor, ":", numeros_divisibles_por_3)
