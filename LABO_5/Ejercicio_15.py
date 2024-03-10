def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def numeros_primos_ordenados(conjunto_numeros):
    primos = {numero for numero in conjunto_numeros if es_primo(numero)}
    primos_ordenados = sorted(primos)
    return primos_ordenados

# Ejemplo de uso
conjunto_numeros = {2, 3, 4, 5, 6, 7, 8, 9, 10}
primos_ordenados = numeros_primos_ordenados(conjunto_numeros)
print("Números primos ordenados:", primos_ordenados)
