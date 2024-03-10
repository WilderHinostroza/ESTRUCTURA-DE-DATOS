def suma(a, b):
    return a + b

try:
    resultado = suma(33, 55)
    assert resultado == 88, f"La función suma debería retornar 88, pero retornó {resultado}."
    print("La función suma retornó el valor esperado.")
except AssertionError as e:
    print(e)
