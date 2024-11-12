class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Clase Stack (Pila) - Implementación LIFO
class Stack:
    def __init__(self):
        self.top = None  # La pila comienza vacía

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise IndexError("Pop from empty stack")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.top is None:
            raise IndexError("Peek from empty stack")
        return self.top.data

    def is_empty(self):
        return self.top is None

# Clase Queue (Cola) - Implementación FIFO
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert(self, data):
        new_node = Node(data)
        if self.rear is None:  # Cola vacía
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def remove(self):
        if self.front is None:
            raise IndexError("Remove from empty queue")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:  # La cola quedó vacía
            self.rear = None
        return data

    def peek(self):
        if self.front is None:
            raise IndexError("Peek from empty queue")
        return self.front.data

    def is_empty(self):
        return self.front is None

# Pruebas para Stack y Queue
def test_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3, "Error en peek() de Stack"
    assert stack.pop() == 3, "Error en pop() de Stack"
    assert stack.pop() == 2, "Error en pop() de Stack"
    assert stack.peek() == 1, "Error en peek() de Stack"
    assert stack.pop() == 1, "Error en pop() de Stack"
    assert stack.is_empty() == True, "Error en is_empty() de Stack"

def test_queue():
    queue = Queue()
    queue.insert(1)
    queue.insert(2)
    queue.insert(3)
    assert queue.peek() == 1, "Error en peek() de Queue"
    assert queue.remove() == 1, "Error en remove() de Queue"
    assert queue.remove() == 2, "Error en remove() de Queue"
    assert queue.peek() == 3, "Error en peek() de Queue"
    assert queue.remove() == 3, "Error en remove() de Queue"
    assert queue.is_empty() == True, "Error en is_empty() de Queue"

# Ejecutar las pruebas
test_stack()
test_queue()
print("Todas las pruebas pasaron correctamente.")
