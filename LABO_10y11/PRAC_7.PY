class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return '0'
    
    stack = Stack()
    
    while decimal_num > 0:
        remainder = decimal_num % 2
        stack.push(remainder)
        decimal_num = decimal_num // 2
    
    binary_str = ''
    while not stack.is_empty():
        binary_str += str(stack.pop())
    
    return binary_str

# Ejemplo de uso
decimal_number = 3
binary_representation = decimal_to_binary(decimal_number)
print(f"El número decimal {decimal_number} en binario es: {binary_representation}")
