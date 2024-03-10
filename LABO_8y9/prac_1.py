def validar_edad(edad):
    assert edad >= 0, "La edad no puede ser un número negativo."
    assert edad >= 18, "Lo siento, eres menor de edad."
    print("¡Bienvenido!")

# Ejemplo
try:
    edad_usuario = int(input("Por favor, ingresa tu edad: "))
    validar_edad(edad_usuario)
except (ValueError, AssertionError) as e:
    print("Edad no válida:", e)
