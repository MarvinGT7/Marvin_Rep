class ColaEspecial(object):
    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # El arreglo almacenado como una lista
        self.__nItems = 0  # Inicialmente, no hay elementos en el arreglo

    def __len__(self):  # Definición especial para la función len()
        return self.__nItems  # Retorna el número de elementos

    def get(self, n):  # Retorna el valor en el índice n
        if 0 <= n < self.__nItems:  # Verifica si n está dentro de los límites
            return self.__a[n]  # Solo retorna el elemento si está dentro de los límites

    def set(self, n, value):  # Establece el valor en el índice n
        if 0 <= n < self.__nItems:  # Verifica si n está dentro de los límites
            self.__a[n] = value  # Solo establece el elemento si está dentro de los límites

    def insert(self, item):  # Inserta el elemento al final
        self.__a[self.__nItems] = item  # El elemento va al final actual
        self.__nItems += 1  # Incrementa el número de elementos

    def find(self, item):  # Encuentra el índice de un elemento
        for j in range(self.__nItems):  # Entre los elementos actuales
            if self.__a[j] == item:  # Si se encuentra,
                return j  # retorna el índice del elemento
        return -1  # No encontrado -> retorna -1

    def search(self, item):  # Busca un elemento
        return self.get(self.find(item))  # y retorna el elemento si se encuentra

    def delete(self, item):  # Elimina la primera aparición de un elemento
        for j in range(self.__nItems):  # Busca entre los elementos actuales
            if self.__a[j] == item:  # Si encuentra el elemento
                self.__nItems -= 1  # Un elemento menos al final
                for k in range(j, self.__nItems):  # Mueve los elementos
                    self.__a[k] = self.__a[k + 1]  # uno a la izquierda
                return True  # Retorna señal de éxito
        return False  # No se encontró el elemento

    def traverse(self, function=print):  # Recorre todos los elementos
        for j in range(self.__nItems):  # y aplica una función
            function(self.__a[j])

    def getMaxNum(self):
        max_num = None  # Inicializa el número máximo como None
        for item in self.__a[:self.__nItems]:  # Itera solo sobre los elementos en uso
            if isinstance(item, (int, float)):  # Verifica si el elemento es un número
                if max_num is None or item > max_num:
                    max_num = item
        return max_num

    def deleteMaxNum(self):
        max_num = None  # Inicializa el número máximo como None
        max_index = -1  # Índice del número máximo

        # Itera sobre los elementos en uso para encontrar el número máximo
        for i in range(self.__nItems):
            item = self.__a[i]
            if isinstance(item, (int, float)):  # Verifica si el elemento es un número
                if max_num is None or item > max_num:
                    max_num = item
                    max_index = i  # Guarda el índice del número máximo

        if max_index != -1:  # Si se encontró un número máximo
            # Elimina el número máximo desplazando los elementos a la izquierda
            for j in range(max_index, self.__nItems - 1):
                self.__a[j] = self.__a[j + 1]
            self.__nItems -= 1  # Reduce el número de elementos
            return max_num  # Retorna el número máximo eliminado

        return None  # Si no se encontró ningún número, retorna None
    
    def insertEspecial(self, item):  # Inserta el elemento al final
        if self.isFull(): # if not full
            raise Exception("Queue overflow")
        self.__a[self.__nItems] = item  # El elemento va al final actual
        self.__nItems += 1  # Incrementa el número de elementos