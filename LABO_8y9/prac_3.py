def validar_calificacion(calificacion):

    assert 0 <= calificacion <= 100, "La calificación debe estar en el rango de 0 a 100."

# Solicitar la calificación al usuario
try:
    calificacion_usuario = float(input("Por favor, ingresa tu calificación: "))
    validar_calificacion(calificacion_usuario)
    print("Calificación válida.")
except ValueError:
    print("Por favor, ingresa un número válido para tu calificación.")
except AssertionError as e:
    print("Calificación no válida:", e)
