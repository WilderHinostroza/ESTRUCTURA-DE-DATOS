from collections import deque

def encontrar_camino_laberinto(laberinto, inicio, fin):
    # Obtener las dimensiones del laberinto
    filas = len(laberinto)
    columnas = len(laberinto[0])

    # Definir direcciones posibles: arriba, abajo, izquierda, derecha
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Inicializar la cola para BFS
    cola = deque([(inicio, 0)])  # Tupla (posición, distancia)
    visitado = set()
    visitado.add(inicio)

    # BFS
    while cola:
        (x, y), distancia = cola.popleft()

        if (x, y) == fin:
            return distancia

        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas and laberinto[nx][ny] != '#' and (nx, ny) not in visitado:
                cola.append(((nx, ny), distancia + 1))
                visitado.add((nx, ny))

    # Si no se encontró un camino
    return None

# Ejemplo de uso
laberinto = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#']
]

inicio = (1, 1)  # Coordenadas de inicio
fin = (3, 6)     # Coordenadas de destino

distancia = encontrar_camino_laberinto(laberinto, inicio, fin)
if distancia is not None:
    print(f"La distancia más corta desde {inicio} hasta {fin} es: {distancia}")
else:
    print(f"No se encontró un camino desde {inicio} hasta {fin}")
