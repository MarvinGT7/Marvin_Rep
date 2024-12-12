class HistorialNavegador:
    def __init__(self):
        self.historial = []

    def visitar(self, url):
        self.historial.append(url)

    def ir_atras(self):
        if self.historial:
            return self.historial.pop()
        return None

# Prueba
historial = HistorialNavegador()
historial.visitar("google.com")
historial.visitar("facebook.com")
historial.visitar("youtube.com")
print(historial.ir_atras())  # Salida: youtube.com
print(historial.ir_atras())  # Salida: facebook.com