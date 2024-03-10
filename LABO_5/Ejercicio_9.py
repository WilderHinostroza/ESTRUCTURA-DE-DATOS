def palabras_con_longitud(conjunto_palabras, longitud):
    return {palabra for palabra in conjunto_palabras if len(palabra) == longitud}

# Ejemplo de uso
conjunto_palabras = {"hola", "adiós", "bien", "mal", "sol", "luna", "cielo", "mar"}
longitud = 3
palabras_de_longitud_3 = palabras_con_longitud(conjunto_palabras, longitud)
print("Palabras de longitud", longitud, ":", palabras_de_longitud_3)
