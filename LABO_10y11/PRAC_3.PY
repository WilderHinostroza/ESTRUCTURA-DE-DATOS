class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 2):
                if current is None:
                    print("La posición excede la longitud de la lista.")
                    return
                current = current.next
            if current is None:
                print("La posición excede la longitud de la lista.")
                return
            new_node.next = current.next
            new_node.prev = current
            if current.next:
                current.next.prev = new_node
            current.next = new_node

    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def print_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

# Crear la lista y agregar nodos
my_list = DoublyLinkedList()
my_list.add_node(1)
my_list.add_node(2)
my_list.add_node(3)
my_list.add_node(4)
my_list.add_node(5)

# Insertar un nuevo nodo en la posición 3 con el dato 15
my_list.insert_at_position(15, 3)

# Imprimir la lista hacia adelante y hacia atrás
print("Lista hacia adelante:")
my_list.print_forward()
print("Lista hacia atrás:")
my_list.print_backward()
