def contar_vocales(cadena):
    # Convertir la cadena a minúsculas para hacer la comparación de manera insensible a mayúsculas y minúsculas
    cadena = cadena.lower()
    # Inicializar un contador para las vocales
    contador_vocales = 0
    # Definir una lista de vocales
    vocales = ['a', 'e', 'i', 'o', 'u']
    # Iterar sobre cada carácter en la cadena
    for caracter in cadena:
        # Verificar si el carácter es una vocal
        if caracter in vocales:
            contador_vocales += 1
    # Devolver el contador de vocales
    return contador_vocales

# Solicitar al usuario que ingrese una cadena de texto
cadena = input("Ingresa una cadena de texto: ")

# Llamar a la función contar_vocales y mostrar el resultado
numero_vocales = contar_vocales(cadena)
print("El número de vocales en la cadena es:", numero_vocales)
