def suma_hasta_n(n):
    if n == 1:
        return 1
    else:
        return n + suma_hasta_n(n - 1)

# Solicitar al usuario que ingrese el valor de n
n = int(input("Ingresa un número entero positivo para calcular la suma hasta ese número: "))

# Calcular la suma de los números del 1 al n llamando a la función recursiva
resultado = suma_hasta_n(n)

# Imprimir el resultado
print("La suma de los números del 1 al", n, "es:", resultado)
