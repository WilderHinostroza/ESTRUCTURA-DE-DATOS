class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()


def evaluar_expresion_posfija(expresion):
    pila = Pila()
    for elemento in expresion.split():
        if elemento.isdigit():  
            pila.apilar(int(elemento))
        else:  
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            if elemento == '+':
                resultado = operando1 + operando2
            elif elemento == '-':
                resultado = operando1 - operando2
            elif elemento == '*':
                resultado = operando1 * operando2
            elif elemento == '/':
                resultado = operando1 / operando2
            pila.apilar(resultado)
    return pila.desapilar()

expresion_posfija = "3 4 + 2 *"
resultado = evaluar_expresion_posfija(expresion_posfija)
print("El resultado de la expresión posfija '{}' es: {}".format(expresion_posfija, resultado))
