def es_palindromo(palabra):
    # Convertir la palabra a minúsculas para hacer la comparación de manera insensible a mayúsculas y minúsculas
    palabra = palabra.lower()
    # Eliminar los espacios en blanco de la palabra
    palabra_sin_espacios = palabra.replace(" ", "")
    # Verificar si la palabra es igual a su inversa
    return palabra_sin_espacios == palabra_sin_espacios[::-1]

# Solicitar al usuario que ingrese una palabra
palabra = input("Ingresa una palabra para verificar si es un palíndromo: ")

# Verificar si la palabra es un palíndromo e imprimir el resultado
if es_palindromo(palabra):
    print(palabra, "es un palíndromo.")
else:
    print(palabra, "no es un palíndromo.")
