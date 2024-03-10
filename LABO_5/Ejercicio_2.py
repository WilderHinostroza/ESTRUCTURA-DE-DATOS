def palabras_con_letra(conjunto_palabras, letra):
    palabras_con_letra = set()
    for palabra in conjunto_palabras:
        if palabra.startswith(letra):
            palabras_con_letra.add(palabra)
    return palabras_con_letra

# Ejemplo de uso
conjunto_palabras = {"manzana", "banana", "pera", "naranja", "sandía", "uva"}
letra = "n"
palabras_con_la_letra_n = palabras_con_letra(conjunto_palabras, letra)
print("Palabras que comienzan con la letra", letra + ":", palabras_con_la_letra_n)
