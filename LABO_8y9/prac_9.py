def saludar():
    
    return "¡Hola!"

try:
    import modulo
    assert hasattr(modulo, 'saludar'), "La función 'saludar' no está disponible en el módulo."
    print("El módulo se ha importado correctamente y contiene la función 'saludar'.")
except ImportError:
    print("Error al importar el módulo 'modulo'.")
except AssertionError as e:
    print(e)
