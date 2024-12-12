def calculadora_pila(operaciones):
    pila = []
    for elemento in operaciones:
        if isinstance(elemento, (int, float)):
            pila.append(elemento)
        else:
            b = pila.pop()
            a = pila.pop()
            if elemento == '+':
                pila.append(a + b)
            elif elemento == '-':
                pila.append(a - b)
            elif elemento == '*':
                pila.append(a * b)
            elif elemento == '/':
                pila.append(a / b)
    return pila.pop()

# Ejemplo
print(calculadora_pila([3, 4, '+', 2, '*', 7, '/']))  # Salida: 2.0
