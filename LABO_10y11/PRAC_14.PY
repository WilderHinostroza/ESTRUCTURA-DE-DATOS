class SistemaDeshacer:
    def __init__(self):
        self.pila_acciones = []
        self.pila_deshaceres = []

    def realizar_accion(self, accion):
        self.pila_acciones.append(accion)
       
        self.pila_deshaceres = []

    def deshacer_accion(self):
        if self.pila_acciones:
            accion_deshacer = self.pila_acciones.pop()
            self.pila_deshaceres.append(accion_deshacer)
            return accion_deshacer
        else:
            return None

    def rehacer_accion(self):
        if self.pila_deshaceres:
            accion_rehacer = self.pila_deshaceres.pop()
            self.pila_acciones.append(accion_rehacer)
            return accion_rehacer
        else:
            return None


sistema = SistemaDeshacer()

sistema.realizar_accion("Escribir texto")
sistema.realizar_accion("Eliminar texto")
sistema.realizar_accion("Copiar texto")

accion_deshacer = sistema.deshacer_accion()
print("Se deshizo la acción:", accion_deshacer)

accion_rehacer = sistema.rehacer_accion()
print("Se rehizo la acción:", accion_rehacer)
