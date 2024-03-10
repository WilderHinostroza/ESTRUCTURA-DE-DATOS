def imprimir_piramide_invertida(n):
    if n > 0:
        # Imprimir espacios en blanco antes de los números
        print(' ' * (n - 1), end='')
        # Imprimir números desde n hasta 1
        print(*range(n, 0, -1))
        # Llamar recursivamente a la función con un número menor
        imprimir_piramide_invertida(n - 1)

# Solicitar al usuario que ingrese el valor de n
n = int(input("Ingresa un número entero positivo para construir la pirámide invertida: "))

# Llamar a la función recursiva para imprimir la pirámide invertida
imprimir_piramide_invertida(n)
