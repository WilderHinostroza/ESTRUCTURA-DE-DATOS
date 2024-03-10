from collections import deque

class SistemaGestionTareas:
    def __init__(self):
        self.tareas_pendientes = deque()
        self.tareas_completadas = set()

    def agregar_tarea(self, tarea):
        self.tareas_pendientes.append(tarea)
        print(f"Tarea '{tarea}' agregada.")

    def completar_tarea(self, tarea):
        if tarea in self.tareas_pendientes:
            self.tareas_pendientes.remove(tarea)
            self.tareas_completadas.add(tarea)
            print(f"Tarea '{tarea}' completada.")
        else:
            print(f"Tarea '{tarea}' no encontrada en las tareas pendientes.")

    def mostrar_proxima_tarea_pendiente(self):
        if self.tareas_pendientes:
            print(f"Próxima tarea pendiente: {self.tareas_pendientes[0]}")
        else:
            print("No hay tareas pendientes.")

# Ejemplo de uso
sistema_tareas = SistemaGestionTareas()
sistema_tareas.agregar_tarea("Limpiar la casa")
sistema_tareas.agregar_tarea("Hacer la compra")
sistema_tareas.agregar_tarea("Hacer ejercicio")
sistema_tareas.mostrar_proxima_tarea_pendiente()
sistema_tareas.completar_tarea("Hacer la compra")
sistema_tareas.mostrar_proxima_tarea_pendiente()
