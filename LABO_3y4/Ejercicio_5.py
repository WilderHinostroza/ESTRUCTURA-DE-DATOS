def tabla_multiplicar(n, i=1):
    if i <= 10:
        print(f"{n} x {i} = {n*i}")
        tabla_multiplicar(n, i + 1)

# Solicitar al usuario que ingrese el número para la tabla de multiplicar
numero = int(input("Ingresa un número para imprimir su tabla de multiplicar: "))

# Imprimir la tabla de multiplicar llamando a la función recursiva
print(f"Tabla de multiplicar del {numero}:")
tabla_multiplicar(numero)
