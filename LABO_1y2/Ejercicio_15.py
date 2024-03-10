def suma_digitos(numero):
    suma = 0
    # Convertir el número en una cadena para iterar sobre sus dígitos
    for digito in str(numero):
        # Convertir cada dígito de vuelta a entero y sumarlo
        suma += int(digito)
    return suma

# Solicitar al usuario que ingrese un número entero
numero_entero = int(input("Ingresa un número entero: "))

# Calcular la suma de los dígitos del número ingresado
resultado = suma_digitos(numero_entero)

# Imprimir el resultado
print("La suma de los dígitos de", numero_entero, "es:", resultado)
