import csv
import os

class Archivo:

    def leer_csv(self,url):
        lista = []
        with open(url, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Salta la primera línea (títulos de columnas)
            for row in reader:
                lista.append(row)
        return lista

    def archivo_existe(self,nombre_archivo):
        return os.path.exists(nombre_archivo)
    
    def archivo_vacio(self,nombre_archivo):
        if self.archivo_existe(nombre_archivo):
            with open(nombre_archivo, 'r') as f:
                return f.read().strip() == ''
        return False