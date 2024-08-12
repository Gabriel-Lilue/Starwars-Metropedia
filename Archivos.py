import csv
import os

class Archivo:

    def leer_csv(self,url):
        """
        Lee un archivo CSV y retorna una lista con los datos.
        Args:
            url (string): URL del archivo CSV.
        Returns:
            list: Lista con los datos del archivo CSV.
        """
        lista = []
        with open(url, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Salta la primera línea (títulos de columnas)
            for row in reader:
                lista.append(row)
        return lista

    def archivo_existe(self):
        """
        Verifica si el archivo Metropedia.txt existe.
        Returns:
            bool: True si el archivo existe, False en caso contrario.
        """
        return os.path.exists('Metropedia.txt')

    def guardar_data(self,misiones):
        """
        Guarda la información de las misiones en un archivo de texto.
        Args:
            misiones (string): Información de las misiones.
        """
        file = open('Metropedia.txt','w')
        string = str(misiones)
        file.write(string)
        file.close()

    def acceder_data(self):
        """
        Accede a la información de las misiones en el archivo de texto.
        Returns:
            list: Lista con la información de las misiones.
        """
        with open('Metropedia.txt','r') as file:
            content = file.read()
            misiones = content.split('\n')
        return misiones
    
    def archivo_vacio(self):
        """
        Verifica si el archivo Metropedia.txt está vacío.
        Returns:
            bool: True si el archivo está vacío, False en caso contrario.
        """
        file = 'Metropedia.txt'
        if not os.path.isfile(file):
            return False
        else:
            with open('Metropedia.txt', "r") as file:
                content = file.read()
                return len(content.strip()) == 0
            
    def listoToString(self,lista):
        """
        Convierte una lista de objetos en un string.
        Args:
            lista (list): Lista de objetos.

        Returns:
            string: String con los nombres de los objetos.
        """
        msg = ''
        for i,element in enumerate(lista):
            if i != len(lista)-1:
                msg += f'{element.name}---'
            else:
                msg += f'{element.name}'
        return msg