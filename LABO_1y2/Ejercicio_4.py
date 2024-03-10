def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Solicitar al usuario que ingrese un número para calcular su factorial
numero = int(input("Ingresa un número para calcular su factorial: "))

# Verificar si el número es negativo
if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    resultado = factorial(numero)
    print("El factorial de", numero, "es:", resultado)
