class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def peek(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def esta_vacia(self):
        return len(self.items) == 0

# Prueba de la clase Pila
pila = Pila()
pila.push(1)
pila.push(2)
pila.push(3)
print(pila.pop())  # Salida: 3
print(pila.peek())  # Salida: 2