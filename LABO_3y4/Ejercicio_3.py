def imprimir_piramide(n, i=1):
    if i <= n:
        # Imprimir números desde 1 hasta i
        print(*range(1, i + 1))
        # Llamar recursivamente a la función con el siguiente nivel de la pirámide
        imprimir_piramide(n, i + 1)

# Solicitar al usuario que ingrese el valor de n
n = int(input("Ingresa un número entero positivo para construir la pirámide: "))

# Llamar a la función recursiva para imprimir la pirámide
imprimir_piramide(n)
