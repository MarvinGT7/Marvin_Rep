from Deque import Deque

deque = Deque()  # Crear una deque sin tamaño máximo

# Insertar elementos en ambos extremos
deque.insertLeft(1)
deque.insertRight(2)
deque.insertLeft(3)
deque.insertRight(4)
deque.insertLeft(5)

print("Contenido del deque después de las inserciones:", deque)

# Eliminar elementos de ambos extremos
print("Elemento eliminado desde la izquierda:", deque.removeLeft())
print("Elemento eliminado desde la derecha:", deque.removeRight())

# Ver contenido actual del deque
print("Contenido del deque después de las eliminaciones:", deque)

# Mostrar los elementos en ambos extremos
print("Elemento en el extremo izquierdo:", deque.peekLeft())
print("Elemento en el extremo derecho:", deque.peekRight())

# Comprobar si la deque está vacía
print("¿Está la deque vacía?", deque.isEmpty())
