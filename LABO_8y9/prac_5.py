class objeto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.edad = precio

objeto1 = objeto("Computadora", 2000)
objeto2 = objeto("Computadora", 3000)

# Validar la igualdad de los objetos
try:
    assert objeto1 == objeto2, "Los objetos no son iguales."
    print("Los objetos son iguales.")
except AssertionError as e:
    print(e)
