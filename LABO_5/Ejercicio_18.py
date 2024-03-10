def palabras_con_letra_ordenadas(conjunto_palabras, letra):
    palabras_con_la_letra = {palabra for palabra in conjunto_palabras if letra in palabra}
    palabras_ordenadas = sorted(palabras_con_la_letra, reverse=True)
    return palabras_ordenadas

# Ejemplo de uso
conjunto_palabras = {"hola", "adiós", "bien", "mal", "sol", "luna", "cielo", "mar"}
letra = "o"
palabras_letra_ordenadas = palabras_con_letra_ordenadas(conjunto_palabras, letra)
print(f"Palabras que contienen la letra '{letra}' ordenadas de mayor a menor:", palabras_letra_ordenadas)
