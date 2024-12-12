def eliminar_duplicados(arreglo):
    unico = []
    for num in arreglo:
        if num not in unico:
            unico.append(num)
    return unico

# Ejemplo
print(eliminar_duplicados([1, 2, 2, 3, 4, 4, 5]))  # Salida: [1, 2, 3, 4, 5]