# Solicitar al usuario que ingrese los números separados por espacios
numeros = input("Ingresa una lista de números separados por espacios: ")

# Convertir la entrada del usuario en una lista de números
numeros = [int(numero) for numero in numeros.split()]

# Ordenar la lista de números de menor a mayor
numeros_ordenados = sorted(numeros)

# Imprimir la lista de números ordenados
print("La lista de números ordenados de menor a mayor es:", numeros_ordenados)
