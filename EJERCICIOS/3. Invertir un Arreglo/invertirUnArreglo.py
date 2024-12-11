def max_min(arreglo):
    max_val = arreglo[0]
    min_val = arreglo[0]
    for num in arreglo:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val

# Ejemplo
print(max_min([3, 1, 4, 1, 5, 9]))  # Salida: (9, 1)