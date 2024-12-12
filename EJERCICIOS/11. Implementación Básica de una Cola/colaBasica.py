class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def peek(self):
        if not self.esta_vacia():
            return self.items[0]
        return None

    def esta_vacia(self):
        return len(self.items) == 0

# Prueba de la clase Cola
cola = Cola()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
print(cola.dequeue())  # Salida: 1
print(cola.peek())  # Salida: 2