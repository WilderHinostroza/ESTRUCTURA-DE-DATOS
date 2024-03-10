from collections import deque

def es_palindroma(palabra):
    # Creamos una cola con los caracteres de la palabra
    cola = deque(palabra)
    
    # Iteramos sobre la mitad de la cola
    while len(cola) > 1:
        # Comparamos el primer y último elemento de la cola
        if cola.popleft() != cola.pop():
            return False
    
    # Si no se encontraron diferencias, la palabra es palíndroma
    return True

# Ejemplo de uso
palabra = "reconocer"
if es_palindroma(palabra):
    print(f'La palabra "{palabra}" es palíndroma.')
else:
    print(f'La palabra "{palabra}" no es palíndroma.')
