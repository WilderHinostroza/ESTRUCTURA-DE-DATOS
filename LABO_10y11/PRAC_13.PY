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

def is_palindrome(word):
    # Eliminar espacios en blanco y convertir a minúsculas
    word = word.replace(" ", "").lower()
    
    stack = Stack()
    for char in word:
        stack.push(char)
    
    # Comparar cada letra con la letra en la pila
    for char in word:
        if char != stack.pop():
            return False
    
    return True

# Ejemplo de uso
words = ["radar", "abba", "A man a plan a canal Panama", "hello"]

for word in words:
    if is_palindrome(word):
        print(f"{word} es un palíndromo.")
    else:
        print(f"{word} no es un palíndromo.")
