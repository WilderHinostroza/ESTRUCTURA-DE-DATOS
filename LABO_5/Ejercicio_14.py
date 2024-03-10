def numeros_no_duplicados(conjunto_numeros):
    duplicados = set()
    no_duplicados = set()
    for numero in conjunto_numeros:
        if numero in no_duplicados:
            no_duplicados.remove(numero)
            duplicados.add(numero)
        elif numero not in duplicados:
            no_duplicados.add(numero)
    return no_duplicados

# Ejemplo de uso
conjunto_numeros = {1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 9, 5}
numeros_no_dupl = numeros_no_duplicados(conjunto_numeros)
print("Números no duplicados:", numeros_no_dupl)
