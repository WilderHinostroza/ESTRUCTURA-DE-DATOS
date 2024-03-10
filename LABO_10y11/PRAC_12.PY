class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()


def evaluar_expresion(tokens):
    pila = Pila()
    for token in tokens:
        if token.isdigit():
            pila.apilar(int(token))
        else:
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            if token == '+':
                resultado = operando1 + operando2
            elif token == '-':
                resultado = operando1 - operando2
            elif token == '*':
                resultado = operando1 * operando2
            elif token == '/':
                resultado = operando1 / operando2
            pila.apilar(resultado)
    return pila.desapilar()


def calcular(expresion):
    tokens = expresion.split()
    resultado = evaluar_expresion(tokens)
    return resultado

expresion = "5 3 + 8 *"
resultado = calcular(expresion)
print("El resultado de la expresión '{}' es: {}".format(expresion, resultado))
