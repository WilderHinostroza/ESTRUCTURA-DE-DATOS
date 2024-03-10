# Definir una función para generar los primeros n números de la serie Fibonacci
def fibonacci(n):
    # Inicializar los primeros dos números de la serie Fibonacci
    fib = [0, 1]
    # Generar los siguientes números de la serie Fibonacci
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

# Generar los primeros 10 números de la serie Fibonacci
primeros_10_fibonacci = fibonacci(10)

# Imprimir los primeros 10 números de la serie Fibonacci
print("Los primeros 10 números de la serie Fibonacci son:")
print(primeros_10_fibonacci)
