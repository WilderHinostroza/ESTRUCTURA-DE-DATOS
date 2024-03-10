def es_palindromo(palabra):
    return palabra == palabra[::-1]

def palabras_palindromos_longitud_ordenadas(conjunto_palabras, longitud):
    palindromos_longitud = {palabra for palabra in conjunto_palabras if es_palindromo(palabra) and len(palabra) == longitud}
    palabras_ordenadas = sorted(palindromos_longitud)
    return palabras_ordenadas

# Ejemplo de uso
conjunto_palabras = {"radar", "civic", "level", "python", "deified", "stats", "madam"}
longitud = 5
palindromos_longitud_ordenadas = palabras_palindromos_longitud_ordenadas(conjunto_palabras, longitud)
print(f"Palíndromos de longitud {longitud} ordenados:", palindromos_longitud_ordenadas)
