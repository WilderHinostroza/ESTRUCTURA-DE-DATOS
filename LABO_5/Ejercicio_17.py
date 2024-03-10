def palabras_con_longitud_ordenadas(conjunto_palabras, longitud):
    palabras_longitud = {palabra for palabra in conjunto_palabras if len(palabra) == longitud}
    palabras_ordenadas = sorted(palabras_longitud)
    return palabras_ordenadas

# Ejemplo de uso
conjunto_palabras = {"hola", "adiós", "bien", "mal", "sol", "luna", "cielo", "mar"}
longitud = 3
palabras_longitud_ordenadas = palabras_con_longitud_ordenadas(conjunto_palabras, longitud)
print(f"Palabras de longitud {longitud} ordenadas:", palabras_longitud_ordenadas)
