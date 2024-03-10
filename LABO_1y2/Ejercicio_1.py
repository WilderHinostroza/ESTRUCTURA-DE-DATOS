# Pedir al usuario que ingrese dos números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Realizar la suma
suma = num1 + num2
print("La suma es:", suma)

# Realizar la resta
resta = num1 - num2
print("La resta es:", resta)

# Realizar la multiplicación
multiplicacion = num1 * num2
print("La multiplicación es:", multiplicacion)

# Realizar la división
# Asegurarse de que el segundo número no sea cero para evitar una división por cero
if num2 != 0:
    division = num1 / num2
    print("La división es:", division)
else:
    print("No se puede dividir por cero.")
