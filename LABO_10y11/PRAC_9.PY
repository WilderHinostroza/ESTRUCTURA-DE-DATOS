class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

def is_valid_expression(expression):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    brackets_map = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty() or brackets_map[char] != stack.pop():
                return False

    return stack.is_empty()

# Ejemplo de uso
expressions = [
    "((x + y) * (z - 5))",
    "{[a + b] * (c - d)}",
    "{(x + y}] * (z - 5)",
    "((x + y) * (z - 5)}"
]

for expr in expressions:
    if is_valid_expression(expr):
        print(f"La expresión '{expr}' está correctamente anidada.")
    else:
        print(f"La expresión '{expr}' no está correctamente anidada.")
