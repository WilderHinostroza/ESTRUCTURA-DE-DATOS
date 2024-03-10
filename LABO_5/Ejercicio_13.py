def encontrar_duplicados(conjunto_numeros):
    duplicados = set()
    unicos = set()
    for numero in conjunto_numeros:
        if numero in unicos:
            duplicados.add(numero)
        else:
            unicos.add(numero)
    return duplicados

# Ejemplo de uso
conjunto_numeros = {1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 9, 5}
duplicados = encontrar_duplicados(conjunto_numeros)
print("Números duplicados:", duplicados)
