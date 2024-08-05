import requests
import os

from Pelicula import Pelicula
from Especie import Especie
from Planeta import Planeta
from Personaje import Personaje

from Nave import Nave
from Vehiculo import Vehiculo
from Arma import Arma

from Mision import Mision

from Archivos import Archivo

class App:
    # Constructor de la clase App
    def __init__(self):
        self.peliculas = []
        self.especies = []
        self.planetas = []
        self.personajes = []
        self.naves = []
        self.vehiculos = []
        self.armas = []
        self.misiones = []

        self.urls = {} # Diccionario de URLs para las APIs

    def get_api_info(self):
        print('\nCargando información... Esta operación puede tomar unos minutos, por favor espere.\n')

        self.get_transporte()
        print('Vehículos y Naves cargados...')
        self.get_peliculas()
        print('Películas cargadas...')
        self.get_planetas()
        print('Planetas cargados...')
        self.get_especies()
        print('Especies cargadas...')
        self.get_personajes()
        print('Personajes cargados...')

        self.actualizar_info()
        # Aqui actualizar las listas de objetos y agregar armas CSV!!!!

    def get_transporte(self):
        pass

    def get_peliculas(self):
        pass

    def get_planetas(self):
        pass

    def get_especies(self):
        pass

    def get_personajes(self):
        pass


    # Algunos atributos vienen con links desde la API, entonces para cambiarlo
    def actualizar_info(self):
        pass