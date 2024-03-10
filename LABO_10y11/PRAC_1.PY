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

    def duplicate_nodes(self):
        current = self.head
        while current:
            duplicate = Node(current.data)
            next_node = current.next
            current.next = duplicate
            duplicate.prev = current
            duplicate.next = next_node
            if next_node:
                next_node.prev = duplicate
            current = next_node

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

# Duplicar los nodos
my_list.duplicate_nodes()

# Imprimir la lista original hacia adelante y hacia atrás
print("Lista original hacia adelante:")
my_list.print_forward()
print("Lista original hacia atrás:")
my_list.print_backward()

# Imprimir la lista duplicada hacia adelante y hacia atrás
print("Lista duplicada hacia adelante:")
my_list.print_forward()
print("Lista duplicada hacia atrás:")
my_list.print_backward()
