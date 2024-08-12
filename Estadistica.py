
class Estadistica:
    def calcular_promedio(self, lista):
        """
        Calcula el promedio de una lista de números.
        Args:
            lista (list): Lista de números.
        Returns:
            float: Promedio de la lista. Si la lista está vacía, devuelve 0.
        """
        if len(lista) == 0:
            return 0
        return sum(lista) / len(lista)

    def valor_maximo(self, lista):
        """
        Obtiene el valor máximo de una lista de números.
        Args:
            lista (list): Lista de números.
        Returns:
            any: Valor máximo de la lista. Si la lista está vacía, devuelve 0.
        """
        if len(lista) == 0:
            return 0
        return max(lista)
    
    def valor_minimo(self, lista):
        """
        Obtiene el valor mínimo de una lista de números.
        Args:
            lista (list): Lista de números.
        Returns:
            any: Valor mínimo de la lista. Si la lista está vacía, devuelve 0.
        """
        if len(lista) == 0:
            return 0
        return min(lista)
        
    def calcular_moda(self,lista):
        """
        Calcula la moda de una lista de valores.
        Args:
            lista (list): Lista de valores.
        Returns:
            moda (any): Valor más frecuente en la lista.
        """
        frecuencias = {}
        for valor in lista:
            if valor in frecuencias:
                frecuencias[valor] += 1
            else:
                frecuencias[valor] = 1
    
        moda = None
        max_frecuencia = 0
        for clave, frecuencia in frecuencias.items():
            if frecuencia > max_frecuencia:
                max_frecuencia = frecuencia
                moda = clave
        return moda
    
    def is_number(self, s):
        """
        Verifica si un número puede ser convertido a número flotante
        Args:
            s (any): número a verificar
        Returns:
            bool: True si s puede ser convertido a número flotante, False en caso contrario
        """
        try:
            float(s)
            return True
        except ValueError:
            return False