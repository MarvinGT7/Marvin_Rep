class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.left = None  # Cabeza del deque
        self.right = None  # Cola del deque
        self.size = 0

    def insertLeft(self, item):
        # Inserta un elemento en el extremo izquierdo (cabeza)
        new_node = Node(item)
        if self.isEmpty():
            self.left = self.right = new_node
        else:
            new_node.next = self.left
            self.left.prev = new_node
            self.left = new_node
        self.size += 1

    def insertRight(self, item):
        # Inserta un elemento en el extremo derecho (cola)
        new_node = Node(item)
        if self.isEmpty():
            self.left = self.right = new_node
        else:
            new_node.prev = self.right
            self.right.next = new_node
            self.right = new_node
        self.size += 1

    def removeLeft(self):
        # Elimina y devuelve el elemento del extremo izquierdo
        if self.isEmpty():
            raise Exception("Deque está vacía")
        item = self.left.value
        if self.left == self.right:  # Si solo hay un elemento
            self.left = self.right = None
        else:
            self.left = self.left.next
            self.left.prev = None
        self.size -= 1
        return item

    def removeRight(self):
        # Elimina y devuelve el elemento del extremo derecho
        if self.isEmpty():
            raise Exception("Deque está vacía")
        item = self.right.value
        if self.left == self.right:  # Si solo hay un elemento
            self.left = self.right = None
        else:
            self.right = self.right.prev
            self.right.next = None
        self.size -= 1
        return item

    def peekLeft(self):
        # Devuelve el elemento del extremo izquierdo sin eliminarlo
        if self.isEmpty():
            raise Exception("Deque está vacía")
        return self.left.value

    def peekRight(self):
        # Devuelve el elemento del extremo derecho sin eliminarlo
        if self.isEmpty():
            raise Exception("Deque está vacía")
        return self.right.value

    def isEmpty(self):
        # Verifica si la deque está vacía
        return self.size == 0

    def __len__(self):
        # Devuelve el número de elementos en la deque
        return self.size

    def __str__(self):
        # Devuelve una representación en cadena de la deque
        elements = []
        current = self.left
        while current is not None:
            elements.append(current.value)
            current = current.next
        return str(elements)
