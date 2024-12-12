def fila_banco(clientes):
    cola = fila_banco()
    for cliente in clientes:
        cola.enqueue(cliente)
    while not cola.esta_vacia():
        print(f"Atendiendo al cliente {cola.dequeue()}")

# Ejemplo
fila_banco(["Cliente 1", "Cliente 2", "Cliente 3"])