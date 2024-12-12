def revertir_cadena(cadena):
    pila = []
    for char in cadena:
        pila.append(char)
    invertida = ""
    while pila:
        invertida += pila.pop()
    return invertida

# Ejemplo
print(revertir_cadena("hola"))  # Salida: "aloh"