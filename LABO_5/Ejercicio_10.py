def palabras_con_letra(conjunto_palabras, letra):
    return {palabra for palabra in conjunto_palabras if letra in palabra}

# Ejemplo de uso
conjunto_palabras = {"hola", "adiós", "bien", "mal", "sol", "luna", "cielo", "mar"}
letra = "o"
palabras_con_la_letra_o = palabras_con_letra(conjunto_palabras, letra)
print("Palabras que contienen la letra", letra + ":", palabras_con_la_letra_o)
