def numeros_comunes(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)

# Ejemplo de uso
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
numeros_en_comun = numeros_comunes(conjunto1, conjunto2)
print("Números en común:", numeros_en_comun)
