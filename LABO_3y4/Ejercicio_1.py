def imprimir_pares(n):
    if n > 0:
        if n % 2 == 0:
            print(n)
        imprimir_pares(n - 1)

# Llamar a la función recursiva con n = 100 para imprimir los números pares del 1 al 100
imprimir_pares(100)
