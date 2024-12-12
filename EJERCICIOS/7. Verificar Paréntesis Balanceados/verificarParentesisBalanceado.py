def verificar_parentesis(cadena):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}
    for char in cadena:
        if char in "({[":
            pila.append(char)
        elif char in ")}]":
            if not pila or pila.pop() != pares[char]:
                return False
    return len(pila) == 0

# Ejemplo
print(verificar_parentesis("{[()]}"))  # Salida: True
print(verificar_parentesis("{[(])}"))  # Salida: False
