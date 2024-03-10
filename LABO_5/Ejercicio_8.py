def es_palindromo(palabra):
    return palabra == palabra[::-1]

def encontrar_palindromos(conjunto_palabras):
    palindromos = {palabra for palabra in conjunto_palabras if es_palindromo(palabra)}
    return palindromos

# Ejemplo de uso
conjunto_palabras = {"radar", "civic", "level", "python", "deified", "stats", "madam"}
palindromos = encontrar_palindromos(conjunto_palabras)
print("Palíndromos encontrados:", palindromos)
