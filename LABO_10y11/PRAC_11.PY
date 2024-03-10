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

def remove_duplicates(stack):
    if stack.is_empty():
        return
    
    temp_stack = Stack()
    unique_elements = set()

    # Transferir elementos únicos a la pila temporal y mantener un registro de elementos únicos
    while not stack.is_empty():
        element = stack.pop()
        if element not in unique_elements:
            temp_stack.push(element)
            unique_elements.add(element)

    # Transferir elementos de la pila temporal nuevamente a la pila original
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

# Ejemplo de uso
original_stack = Stack()
original_stack.push(1)
original_stack.push(2)
original_stack.push(3)
original_stack.push(2)
original_stack.push(4)
original_stack.push(1)

print("Pila original:")
while not original_stack.is_empty():
    print(original_stack.pop(), end=" ")

remove_duplicates(original_stack)

print("\nPila sin duplicados:")
while not original_stack.is_empty():
    print(original_stack.pop(), end=" ")
