def buscar_elemento(arreglo, elemento):
    for num in arreglo:
        if num == elemento:
            return True
    return False

# Ejemplo
print(buscar_elemento([1, 2, 3, 4, 5], 3))  # Salida: True