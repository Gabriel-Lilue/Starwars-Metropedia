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

    def archivo_existe(self):
        return os.path.exists('Metropedia.txt')

    def guardar_data(self,misiones):
        file = open('Metropedia.txt','w')
        string = str(misiones)
        file.write(string)
        file.close()

    def acceder_data(self):
        with open('Metropedia.txt','r') as file:
            content = file.read()
            misiones = content.split('\n')
        return misiones
    
    def archivo_vacio(self):
        file = 'Metropedia.txt'
        if not os.path.isfile(file):
            return False
        else:
            with open('Metropedia.txt', "r") as file:
                content = file.read()
                return len(content.strip()) == 0
            
    def listoToString(self,lista):
        msg = ''
        for i,element in enumerate(lista):
            if i != len(lista)-1:
                msg += f'{element.name}---'
            else:
                msg += f'{element.name}'
        return msg