def es_palindromo(palabra):
    return palabra == palabra[::-1]

def palabras_palindromos_ordenadas(conjunto_palabras):
    palindromos = {palabra for palabra in conjunto_palabras if es_palindromo(palabra)}
    palindromos_ordenados = sorted(palindromos)
    return palindromos_ordenados

# Ejemplo de uso
conjunto_palabras = {"radar", "civic", "level", "python", "deified", "stats", "madam"}
palindromos_ordenados = palabras_palindromos_ordenadas(conjunto_palabras)
print("Palíndromos ordenados:", palindromos_ordenados)
