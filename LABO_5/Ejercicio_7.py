def encontrar_anagramas(conjunto_palabras):
    anagramas = {}
    for palabra in conjunto_palabras:
        palabra_ordenada = ''.join(sorted(palabra))
        if palabra_ordenada in anagramas:
            anagramas[palabra_ordenada].add(palabra)
        else:
            anagramas[palabra_ordenada] = {palabra}
    # Filtrar y devolver solo los conjuntos con más de una palabra (anagramas)
    return {tuple(valores) for valores in anagramas.values() if len(valores) > 1}

# Ejemplo de uso
conjunto_palabras = {"gato", "toga", "amor", "roma", "mora", "perro", "roper", "arrop"}
conjunto_anagramas = encontrar_anagramas(conjunto_palabras)
print("Conjunto de anagramas:")
for anagrama in conjunto_anagramas:
    print(anagrama)
