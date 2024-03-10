def diferencia_conjuntos(conjunto1, conjunto2):
    return conjunto2.difference(conjunto1)

# Ejemplo de uso
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
diferencia = diferencia_conjuntos(conjunto1, conjunto2)
print("Diferencia entre conjunto2 y conjunto1:", diferencia)
