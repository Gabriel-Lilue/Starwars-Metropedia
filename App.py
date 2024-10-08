import requests
import os

import matplotlib.pyplot as plt

from Estadistica import Estadistica
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
    def __init__(self):
        """
        Inicializa las listas de objetos y el diccionario de URLs.
        """
        self.peliculas = []
        self.especies = []
        self.planetas = []
        self.personajes = []
        self.naves = []
        self.vehiculos = []
        self.armas = []
        self.misiones = []

        self.urls = {} # Diccionario de URLs para las APIs

    # CENTRALIZAR FUNCIONES DE LA API
    def get_api_info(self):
        """
        Centraliza las funciones que obtienen la información de la API de Star Wars.
        """
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
        self.csv_info() # Aqui actualizar las listas de objetos y agregar armas
        print('Información actualizada...')
        self.continuar()
    

    # FUNCIONES UTILES
    def add_URLs(self, name, url):
        """
        Añade una URL al diccionario de URLs.
        Args:
            name (string): Nombre de la clave asociada al URL
            url (string): URL a añadir.
        """
        self.urls[name] = url
    
    def find_URLs_match(self, url):
        """
        Busca una URL en el diccionario de URLs y devuelve la clave asociada.
        Args:
            url (string): URL a buscar.
        Returns:
            name (string): Nombre asociado a la URL. Si no se encuentra, devuelve None.
        """
        for name, url_match in self.urls.items():
            if url_match == url:
                return name
        return None
            
    def return_list(self, lista):
        """
        Reemplaza las URLs de una lista por los nombres asociados en el diccionario de URLs.
        Args:
            lista (list): Lista de URLs.
        Returns:
            lista (list): Lista con los nombres asociados a las URLs.
        """
        if len(lista) != 0:
            for url in lista:
                name = self.find_URLs_match(url)
                if name is not None:
                    lista[lista.index(url)] = name
        return lista

    def get_all_items(self, url):
        """
        Obtiene todos los elementos de una API que contiene una paginación. Permite navegar las páginas de la API.
        Args:
            url (string): URL de la API.
        Returns:
            lista (list): Lista con todos los elementos de la API.
        """
        lista = []
        while True:
            response = requests.get(url)
            data = response.json()
            lista.extend(data['results'])
            if data.get('next') is None:
                break
            url = data['next']  # Actualizamos la URL para la próxima página
            response = requests.get(url)  # Hacemos la petición a la próxima página
        return lista

    def buscar_objeto(self, id, lista):
        """
        Busca un objeto en una lista por su ID.
        Args:
            id (int): ID del objeto a buscar.
            lista (list): Lista de objetos.

        Returns:
            elemento: Objeto encontrado. Si no se encuentra, devuelve None.
        """
        for elemento in lista:
            if int(elemento.id) == id:
                return elemento
        return None
    
    def buscar_objeto2(self, name, lista):
        """
        Busca un objeto en una lista por su nombre.
        Args:
            name (string): Nombre del objeto a buscar.
            lista (list): Lista de objetos.
        Returns:
            elemento: Objeto encontrado. Si no se encuentra, devuelve None.
        """
        for elemento in lista:
            if elemento.name == name:
                return elemento
        return None


    # OBTENER INFORMACION DE LA API
    def get_transporte(self):
        """
        Obtiene la información de vehículos y naves de la API de Star Wars.
        """

        # VEHICULOS
        url = 'https://swapi.dev/api/vehicles/' # URL de la API de vehículos
        vehiculos = self.get_all_items(url) # Obtenemos todos los vehiculos de la API
        
        for vehiculo in vehiculos:
            # Por cada elemento se obtiene la información de cada variable y se crea un objeto
            id = len(self.vehiculos) + 1
            name = vehiculo['name']
            model = vehiculo['model']
            manufacturer = vehiculo['manufacturer']
            cost_in_credits = vehiculo['cost_in_credits']
            length = vehiculo['length']
            max_atmosphering_speed = vehiculo['max_atmosphering_speed']
            cargo_capacity = vehiculo['cargo_capacity']
            vehicle_class = vehiculo['vehicle_class']

            # Se añade la URL al diccionario de URLs para su búsqueda más adelante
            self.add_URLs(name, vehiculo['url'])

            # Se añade el objeto a la lista de vehiculos
            self.vehiculos.append(Vehiculo(id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,cargo_capacity,vehicle_class))

        # NAVES
        url = 'https://swapi.dev/api/starships/'
        naves = self.get_all_items(url)
        # self, id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,cargo_capacity,hyperdrive_rating,MGLT,starship_class
        for nave in naves:
            id = len(self.naves) + 1
            name = nave['name']
            model = nave['model']
            manufacturer = nave['manufacturer']
            cost_in_credits = nave['cost_in_credits']
            length = nave['length']
            max_atmosphering_speed = nave['max_atmosphering_speed']
            cargo_capacity = nave['cargo_capacity']
            hyperdrive_rating = nave['hyperdrive_rating']
            MGLT = nave['MGLT']
            starship_class = nave['starship_class']

            self.add_URLs(name, nave['url'])

            self.naves.append(Nave(id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,cargo_capacity,hyperdrive_rating,MGLT,starship_class))

    def get_peliculas(self):
        """
        Obtiene la información de las películas de la API de Star Wars.
        """
        url = 'https://swapi.dev/api/films/'
        peliculas = self.get_all_items(url)
        for pelicula in peliculas:
            id = len(self.peliculas) + 1
            title = pelicula['title']
            episode_id = pelicula['episode_id']
            opening_crawl = pelicula['opening_crawl']
            director = pelicula['director']
            producer = pelicula['producer']
            release_date = pelicula['release_date']
            
            self.add_URLs(title, pelicula['url'])
            self.peliculas.append(Pelicula(id,title,episode_id,release_date ,opening_crawl,director,producer))

    def get_especies(self):
        """
        Obtiene la información de las especies de la API de Star Wars.
        """
        url = 'https://swapi.dev/api/species/'
        especies = self.get_all_items(url)
        for especie in especies:
            # self, id, name, classification, designation, average_height, skin_colors, hair_colors, eye_colors, average_lifespan, language, homeworld
            id = len(self.especies) + 1
            name = especie['name']
            classification = especie['classification']
            designation = especie['designation']
            average_height = especie['average_height']
            skin_colors = especie['skin_colors']
            hair_colors = especie['hair_colors']
            eye_colors = especie['eye_colors']
            average_lifespan = especie['average_lifespan']
            language = especie['language']

            homeworld = especie['homeworld']
            if homeworld is not None:
                homeworld_name = self.find_URLs_match(homeworld)
                if homeworld_name is not None:
                    homeworld = homeworld_name
            else:
                homeworld = 'Unknown'

            people = especie['people'] # Lista de URLs de personajes
            
            films = self.return_list(especie['films']) # Lista de URLs de películas

            self.add_URLs(name, especie['url'])

            self.especies.append(Especie(id,name,classification,designation,average_height,skin_colors,hair_colors,eye_colors,average_lifespan,language,homeworld,people,films))

    def get_planetas(self):
        """
        Obtiene la información de los planetas de la API de Star Wars.
        """
        url = 'https://swapi.dev/api/planets/'
        planetas = self.get_all_items(url)
        # self, id,name,diameter,rotation_period,orbital_period,gravity,population,climate,terrain,surface_water,residents,films
        for planeta in planetas:
            id = len(self.planetas) + 1
            name = planeta['name']
            diameter = planeta['diameter']
            rotation_period = planeta['rotation_period']
            orbital_period = planeta['orbital_period']
            gravity = planeta['gravity']
            population = planeta['population']
            climate = planeta['climate']
            terrain = planeta['terrain']
            surface_water = planeta['surface_water']

            residents = planeta['residents'] # Lista de URLs de personajes
            
            films = self.return_list(planeta['films'])
            

            self.add_URLs(name, planeta['url'])

            self.planetas.append(Planeta(id,name,diameter,rotation_period,orbital_period,gravity,population,climate,terrain,surface_water,residents,films))

    def get_personajes(self):
        """
        Obtiene la información de los personajes de la API de Star Wars.
        """
        url = 'https://swapi.dev/api/people/'
        personajes = self.get_all_items(url)
        # id, name, species, gender, films, homeworld, starships, vehicles
        for personaje in personajes:
            id = len(self.personajes) + 1

            name = personaje['name']
            species = personaje['species']
            if species != []:
                species = species[0]
                species_name = self.find_URLs_match(species)
                if species_name is not None:
                    species = species_name
            else:
                species = 'Unknown'

            gender = personaje['gender']

            films = self.return_list(personaje['films'])

            homeworld = personaje['homeworld']
            if homeworld is not None:
                homeworld_name = self.find_URLs_match(homeworld)
                if homeworld_name is not None:
                    homeworld = homeworld_name
            else:
                homeworld = 'Unknown'

            starships = self.return_list(personaje['starships'])
            vehicles = self.return_list(personaje['vehicles'])

            self.add_URLs(name, personaje['url'])

            self.personajes.append(Personaje(id,name,species,gender,films,homeworld,starships,vehicles))

    def actualizar_info(self):
        """
        Actualiza la información de los objetos con los nombres de las URLs.
        """
        # Actualizamos la información de los objetos

        # ESPECIES
        for especie in self.especies:
            # Personas
            for i, persona_url in enumerate(especie.people):
                persona_name = self.find_URLs_match(persona_url)
                if persona_name is not None:
                    especie.people[i] = persona_name
        
        # PLANETAS
        for planeta in self.planetas:
            # Personas
            for i, persona_url in enumerate(planeta.residents):
                persona_name = self.find_URLs_match(persona_url)
                if persona_name is not None:
                    planeta.residents[i] = persona_name

    def csv_info(self):
        """
        Actualiza la información de los objetos y listas con los archivos CSV
        """
        # Aqui se agregan las armas
        archivo = Archivo()
        armas = archivo.leer_csv('csv/weapons.csv')
        for arma in armas:
            id = int(arma[0])
            name = arma[1]
            model = arma[2]
            manufacturer = arma[3]
            cost_in_credits = arma[4]
            length = arma[5]
            weapon_type = arma[6]
            description = arma[7]
            films = arma[8]

            self.armas.append(Arma(id,name,model,manufacturer,cost_in_credits,length,weapon_type,description,films))

        # Verificar información de los objetos

        # PELICULAS
        peliculas_csv = archivo.leer_csv('csv/films.csv')
        ids = []
        for pelicula in self.peliculas:
            for pelicula_csv in peliculas_csv: 
                if pelicula.episode_id == pelicula_csv[0]:
                    pelicula.title = pelicula_csv[1]
                    ids.append(pelicula.episode_id)
        
        for pelicula_csv in peliculas_csv:
            if pelicula_csv[0] not in ids:
                id = len(self.peliculas) + 1
                title = pelicula_csv[1]
                episode_id = pelicula_csv[0]
                release_date = pelicula_csv[2]
                opening_crawl = pelicula_csv[3]
                director = pelicula_csv[4]
                producer = pelicula_csv[5]

                self.peliculas.append(Pelicula(id,title,episode_id,release_date,opening_crawl,director,producer))

        # ESPECIES
        especies_csv = archivo.leer_csv('csv/species.csv')
        names = []
        for especie in self.especies:
            names.append(especie.name)

        for especie_csv in especies_csv:
            if especie_csv[1] not in names:
                id = len(self.especies) + 1
                # id,name,classification,designation,average_height,skin_colors,hair_colors,eye_colors,average_lifespan,language,homeworld
                name = especie_csv[1]
                classification = especie_csv[2]
                designation = especie_csv[3]
                average_height = especie_csv[4]
                skin_colors = especie_csv[5]
                hair_colors = especie_csv[6]
                eye_colors = especie_csv[7]
                average_lifespan = especie_csv[8]
                language = especie_csv[9]
                homeworld = especie_csv[10]

                people = ["No definido"]
                films = ["No definido"]

                self.especies.append(Especie(id,name,classification,designation,average_height,skin_colors,hair_colors,eye_colors,average_lifespan,language,homeworld,people,films))
        
        # PLANETAS
        planetas_csv = archivo.leer_csv('csv/planets.csv')
        names = []
        for planeta in self.planetas:
            names.append(planeta.name)
        
        for planeta_csv in planetas_csv:
            if planeta_csv[1] not in names:
                id = len(self.planetas) + 1
                # id,name,diameter,rotation_period,orbital_period,gravity,population,climate,terrain,surface_water,residents,films
                name = planeta_csv[1]
                diameter = planeta_csv[2]
                rotation_period = planeta_csv[3]
                orbital_period = planeta_csv[4]
                gravity = planeta_csv[5]
                population = planeta_csv[6]
                climate = planeta_csv[7]
                terrain = planeta_csv[8]
                surface_water = planeta_csv[9]

                if "," in planeta_csv[10]:
                    residents = planeta_csv[10].split(",")
                else:
                    residents = [planeta_csv[10]]
                    for r in residents:
                        r = r.strip()
                
                if "," in planeta_csv[11]:
                    films = planeta_csv[11].split(",")
                    for f in films:
                        f = f.strip()
                else:
                    [planeta_csv[11]]
                    

                self.planetas.append(Planeta(id,name,diameter,rotation_period,orbital_period,gravity,population,climate,terrain,surface_water,residents,films))
            else:
                if "," in planeta_csv[10]:
                    residents = planeta_csv[10].split(",")
                else:
                    residents = [planeta_csv[10]]

                planeta_modificar = self.buscar_objeto2(planeta_csv[1], self.planetas)
                for resident in residents:
                    if resident not in planeta_modificar.residents:
                        planeta_modificar.residents.append(resident.strip())
        # PERSONAJES
        personajes_csv = archivo.leer_csv('csv/characters.csv')
        names = []
        for personaje in self.personajes:
            names.append(personaje.name)

        
        for personaje_csv in personajes_csv:
            if personaje_csv[1] not in names:
                id = len(self.personajes) + 1
                name = personaje_csv[1]
                species = personaje_csv[2]
                gender = personaje_csv[3]
                films = personaje_csv[4].split(",")
                homeworld = personaje_csv[10]

                for planeta in self.planetas:
                    if homeworld == planeta.name:
                        if name not in planeta.residents:
                            planeta.residents.append(name)

                starships = ["No definido"]
                vehicles = ["No definido"]

                self.personajes.append(Personaje(id,name,species,gender,films,homeworld,starships,vehicles))

        # NAVES
        naves_csv = archivo.leer_csv('csv/starships.csv')
        names = []
        for nave in self.naves:
            names.append(nave.name)

        for nave_csv in naves_csv:
            if nave_csv[1] not in names:
                id = len(self.naves) + 1
                name = nave_csv[1]
                model = nave_csv[2]
                manufacturer = nave_csv[3]

                if not nave_csv[4].isspace():
                    cost_in_credits = nave_csv[4]
                else:
                    cost_in_credits = "unknown"

                if not nave_csv[5].isspace():
                    length = nave_csv[5]
                else:
                    length = "unknown"
                
                if not nave_csv[6].isspace():
                    max_atmosphering_speed = nave_csv[6]
                else:
                    max_atmosphering_speed = "unknown"
                
                if not nave_csv[9].isspace():
                    cargo_capacity = nave_csv[9]
                else:
                    cargo_capacity = "unknown"
                
                if not nave_csv[11].isspace():
                    hyperdrive_rating = nave_csv[11]
                else:
                    hyperdrive_rating = "unknown"
                
                if not nave_csv[12].isspace():
                    MGLT = nave_csv[12]
                else:
                    MGLT = "unknown"

                starship_class = nave_csv[13]

                self.naves.append(Nave(id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,cargo_capacity,hyperdrive_rating,MGLT,starship_class))

        # VEHICULOS
        vehiculos_csv = archivo.leer_csv('csv/vehicles.csv')
        names = []
        for vehiculo in self.vehiculos:
            names.append(vehiculo.name)
        
        for vehiculo_csv in vehiculos_csv:
            if vehiculo_csv[1] not in names:
                id = len(self.vehiculos) + 1
                name = vehiculo_csv[1]
                model = vehiculo_csv[2]
                manufacturer = vehiculo_csv[3]
                cost_in_credits = vehiculo_csv[4]
                length = vehiculo_csv[5]
                max_atmosphering_speed = vehiculo_csv[6]
                cargo_capacity = vehiculo_csv[9]
                vehicle_class = vehiculo_csv[11]

                self.vehiculos.append(Vehiculo(id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,cargo_capacity,vehicle_class))


    # FUNCIONES DE MOSTRAR
    def mostrar_armas(self):
        """
        Muestra las armas disponibles.
        """
        for arma in self.armas:
            print(arma.show())
    
    def mostrar_personajes(self):
        """
        Muestra los personajes disponibles
        """
        for i,personaje in self.personajes:
            print(personaje.show())
            if i == 100:
                self.continuar()

    def mostrar_peliculas(self):
        """
        Muestra las películas disponibles.
        """
        for pelicula in self.peliculas:
            print(pelicula.show())

    def mostrar_especies(self):
        """
        Muestra las especies disponibles.
        """
        for especie in self.especies:
            print(especie.show())

    def mostrar_planetas(self):
        """
        Muestra los planetas disponibles.
        """
        for planeta in self.planetas:
            print(planeta.show())

    def mostrar_naves(self):
        """
        Muestra las naves disponibles.
        """
        for nave in self.naves:
            print(nave.show())


    # FUNCIONES DE BUSCAR
    def buscar_personajes(self):
        """
        Permite la búsqueda de los personajes ingresando caracteres que puedan coincidir
        """
        while True:
            print('\nBÚSQUEDA DE PERSONAJES')
            name = input('Ingrese el nombre del personaje deseado -> ').lower() # Solicita al usuario el nombre del personaje a buscar

            results = []
            for personaje in self.personajes:
                if name in personaje.name.lower(): # Para poder buscar por caracteres en común (no necesariamente el nombre exacto)
                    results.append(personaje)

            if len(results) == 0:
                ans = input('No hay coincidencias.\n¿Desea reintentar? [y/n] --> ') # Oportunidad de reintentar en caso de que no hayan coincidencias
                while ans.lower() not in ['y','n']:
                    ans = input('Error...\n¿Desea reintentar? [y/n] --> ')
                if ans.lower() == 'n':
                    break
            else:
                print('\nSe han encontrado las siguientes coincidencias:\n')
                for p in results:
                    print(p.show()) # Se muestran las coincidencias con lo ingresado

                ans = input('¿Desea buscar otro personaje? [y/n] --> ')
                while ans.lower() not in ['y','n']:
                    ans = input('Error...\n¿Desea buscar otro personaje? [y/n] --> ')
                if ans.lower() == 'n':
                    break

    def buscar_personajes2(self, lista_personajes):
        """
        Permite la búsqueda de personajes ingresando su ID.
        Args:
            lista_personajes (list): Lista de personajes a excluir de la búsqueda.
        Returns:
            Objeto (Personaje): Personaje encontrado. Si no se encuentra, devuelve None.
        """
        for personaje in self.personajes:
            if personaje not in lista_personajes:
                print(personaje.show())

        while True:
            personaje_seleccion = input('Ingrese el ID del personaje deseado -> ')

            while not personaje_seleccion.isnumeric(): # Validacion
                personaje_seleccion = input('Error...\nIngrese el ID del personaje deseado -> ')

            for personaje in self.personajes:
                if personaje.id == int(personaje_seleccion):
                    print('Personaje encontrado...\n')
                    print(personaje.show())
                    input('Presione ENTER para continuar...')
                    return personaje
                
            print('Personaje no encontrado...\n')
            ans = input('¿Desea reintentar? [y/n] --> ')
            while ans.lower() not in ['y','n']:
                ans = input('Error...\n¿Desea reintentar? [y/n] --> ')
            if ans.lower() == 'n':
                break
        return None

    def buscar_planeta(self):
        """
        Permite la búsqueda de un planeta ingresando su ID.
        Returns:
            Objeto (Planeta): Planeta encontrado. Si no se encuentra, devuelve None.
        """
        self.mostrar_planetas()
        while True:
            planeta_seleccion = input('Ingrese el ID del planeta destino -> ')
            while not planeta_seleccion.isnumeric():
                planeta_seleccion = input('Error...\nIngrese el ID del planeta destino -> ')

            for planeta in self.planetas:
                if planeta.id== int(planeta_seleccion):
                    print('Planeta encontrado...\n')
                    print(planeta.show())
                    self.continuar()
                    return planeta
                
            print('Planeta no encontrado...\n')
            ans = input('¿Desea reintentar? [y/n] --> ')
            while ans.lower() not in ['y','n']:
                ans = input('Error...\n¿Desea reintentar? [y/n] --> ')
            if ans.lower() == 'n':
                break

        return None
    
    def buscar_nave(self):
        """
        Permite la búsqueda de una nave ingresando su ID.
        Returns:
            Objeto (Nave): Nave encontrada. Si no se encuentra, devuelve None.
        """
        self.mostrar_naves()
        while True:
            nave_seleccion = input('Ingrese el ID de la nave a utilizar -> ')

            while not nave_seleccion.isnumeric():
                nave_seleccion = input('Error...\nIngrese el ID de la nave a utilizar -> ')

            for nave in self.naves:
                if nave.id== int(nave_seleccion):
                    print('Nave encontrada...\n')
                    print(nave.show())
                    self.continuar()
                    return nave
                
            print('Nave no encontrada...\n')
            ans = input('¿Desea reintentar? [y/n] --> ')
            while ans.lower() not in ['y','n']:
                ans = input('Error...\n¿Desea reintentar? [y/n] --> ')
            if ans.lower() == 'n':
                break

        return None

    def buscar_arma(self, lista_armas):
        """
        Permite la búsqueda de un arma ingresando su ID.
        Args:
            lista_armas (list): Lista de armas a excluir de la búsqueda.
        Returns:
            Objeto (Arma): Arma encontrada. Si no se encuentra, devuelve None.
        """
        print("Lista de armas disponibles:")
        for arma in self.armas:
            if arma not in lista_armas:
                print(arma.show())

        while True:
            arma_seleccion = input('Ingrese el ID del arma a utilizar -> ')
            while not arma_seleccion.isnumeric():
                arma_seleccion = input('Error...\nIngrese el ID del arma a utilizar -> ')

            arma_encontrada = False
            for arma in self.armas:
                if arma.id == int(arma_seleccion):
                    print('Arma encontrada...\n')
                    print(arma.show())  # Mostrar los detalles del arma encontrada
                    input('Presione ENTER para continuar...')
                    return arma

            if not arma_encontrada:
                print('Arma no encontrada...\n')
                ans = input('¿Desea reintentar? [y/n] --> ')
                while ans.lower() not in ['y', 'n']:
                    ans = input('Error...\n¿Desea reintentar? [y/n] --> ')
                if ans.lower() == 'n':
                    break

        return None


    # FUNCIONES DE MISIONES
    def txt_a_mision(self):
        """
        Convierte el archivo de texto a una lista de misiones.
        """
        lista_misiones_txt = Archivo().acceder_data()
        if lista_misiones_txt[len(lista_misiones_txt) - 1] == "": # Al guardar de misiones a txt, se guarda con un salto de linea vacio, aqui se elimina
            lista_misiones_txt.pop()

        for mision_txt in lista_misiones_txt:
            mision = mision_txt.split(",") # Separo mi texto por comas, convirtiendolo en lista donde cada elemento es un atributo
            id = int(mision[0])
            name = mision[1]
            destination = self.buscar_objeto2(mision[2], self.planetas) # Busco el objeto
            spaceship = self.buscar_objeto2(mision[3], self.naves) # Busco el objeto

            weapons_txt = mision[4].split("---") # Los personajes y armas estan divididos asi, los separo y convierto en lineas
            weapons = []
            for weapon in weapons_txt:
                arma = self.buscar_objeto2(weapon, self.armas) # Busco el objeto
                if arma is not None:
                    weapons.append(arma)

            characters_txt = mision[5].split("---")
            characters = []
            for character in characters_txt:
                personaje = self.buscar_objeto2(character, self.personajes)
                if personaje is not None:
                    characters.append(personaje)

            self.misiones.append(Mision(id,name,destination,spaceship,weapons,characters)) # Agrego la mision al sistema
            # print(Mision(id,name,destination,spaceship,weapons,characters).show())

    def mision_a_txt(self):
        """
        Convierte la lista de misiones a un archivo de texto
        """
        misiones_txt = ""
        archivo = Archivo()

        for mision in self.misiones:
            mision_string = ""

            mision_string += f"{mision.id},{mision.name},{mision.destination.name},{mision.spaceship.name},{archivo.listoToString(mision.weapons)},{archivo.listoToString(mision.characters)}"
            misiones_txt += mision_string + "\n"

        archivo.guardar_data(misiones_txt)
        
    def datos_mision(self,mision):
        """
        Muestra los datos de una misión.
        Args:
            mision (Mision): Misión a mostrar.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print(mision.show())
        print('\nDatos Específicos\n')
        mision.show_destination()
        mision.show_spaceship()
        mision.show_weapons()
        mision.show_characters()
    
    def modificar_mision(self,mision):
        """
        Permite modificar una misión.
        Args:
            mision (Mision): Misión a modificar.
        """
        print('\nMODIFICAR MISIÓN\n')
        print(mision.show())

        while True:
            opcion = input('''¿Qué deseas modificar?
1. Armas a Utilizar
2. Integrantes de la Misión
3. Nave a Utilizar
4. Planeta Destino
5. Volver
--> ''')
            while not opcion.isnumeric() or int(opcion) not in [1,2,3,4,5]:
                opcion = input('Error...\n¿Qué deseas modificar? --> ')

            if opcion == "1": # ARMAS
                opcion_armas = input('\nMODIFICAR ARMAS\n1. Agregar\n2. Eliminar\n3. Volver\n--> ')
                while not opcion_armas.isnumeric() or int(opcion_armas) not in [1,2,3]:
                    opcion_armas = input('Error...\n¿Qué deseas hacer? --> ')
                
                if opcion_armas == "1": # AGREGAR
                    if len(mision.weapons) != 7: # Maximo de armas que se pueden tener
                        print('\nARMAS DISPONIBLES\n')
                        for arma in self.armas:
                            print(arma.show())
                        arma = self.buscar_arma(mision.weapons)
                        if arma is not None and arma not in mision.weapons:
                            mision.weapons.append(arma)
                            print('Arma agregada...\n')
                            print(mision.show())
                        else:
                            print('Arma no encontrada o ya se encuentra agregada...\n')
                    else:
                        print('No puedes agregar más armas... (Máximo 7)\n')

                elif opcion_armas == "2": # ELIMINAR
                    if len(mision.weapons) != 1:
                        print('\nARMAS DE LA MISIÓN\n')
                        for arma in mision.weapons:
                            print(arma.show())

                        arma_seleccion = input('Ingrese el ID del arma a eliminar -> ')
                        while not arma_seleccion.isnumeric():
                            arma_seleccion = input('Error...\nIngrese el ID del arma a eliminar -> ')

                        arma = self.buscar_objeto(int(arma_seleccion), mision.weapons)
                        if arma is not None:
                            mision.weapons.remove(arma)
                            print('Arma eliminada...\n')
                            print(mision.show())
                        else:
                            print('Arma no encontrada...\n')
                    else:
                        print('Debe haber al menos 1 arma...\n')
                
            elif opcion =="2": # INTEGRANTES
                opcion_personajes = input('\nMODIFICAR INTEGRANTES\n1. Agregar\n2. Eliminar\n3. Volver\n--> ')
                while not opcion_personajes.isnumeric() or int(opcion_personajes) not in [1,2,3]:
                    opcion_personajes = input('Error...\n¿Qué deseas hacer? --> ')
                
                if opcion_personajes == "1": # AGREGAR
                    if len(mision.characters) != 7:
                        print('\nPERSONAJES DISPONIBLES\n')
                        for personaje in self.personajes:
                            print(personaje.show())
                        personaje = self.buscar_personajes2(mision.characters)
                        if personaje is not None and personaje not in mision.characters:
                            mision.characters.append(personaje)
                            print('Personaje agregado...\n')
                            print(mision.show())
                        else:
                            print('Personaje no encontrado o ya se encuentra agregado...\n')
                    else:
                        print('No puedes agregar más personajes... (Máximo 7)\n')

                elif opcion_personajes == "2": # ELIMINAR
                    if len(mision.characters) != 1:
                        print('\nPERSONAJES DE LA MISIÓN\n')
                        for personaje in mision.characters:
                            print(personaje.show())

                        personaje_seleccion = input('Ingrese el ID del personaje a eliminar -> ')
                        while not personaje_seleccion.isnumeric():
                            personaje_seleccion = input('Error...\nIngrese el ID del personaje a eliminar -> ')

                        personaje = self.buscar_objeto(int(personaje_seleccion), mision.characters)
                        if personaje is not None:
                            mision.characters.remove(personaje)
                            print('Personaje eliminado...\n')
                            print(mision.show())
                        else:
                            print('Personaje no encontrado...\n')
                    else:
                        print('Debe haber al menos 1 integrante...\n')
            
            elif opcion == "3": # NAVE
                print('\nNAVES DISPONIBLES\n')
                nave_seleccion = self.buscar_nave()
                if nave_seleccion is not None:
                    if nave_seleccion.id != mision.spaceship.id:
                        mision.spaceship = nave_seleccion
                        print('Nave modificada...\n')
                        print(mision.show())
                    else:
                        print('La nave ya se encuentra seleccionada...\n')
                else:
                    print('Nave no encontrada...\n')

            elif opcion == "4": # PLANETA
                print('\nPLANETAS DISPONIBLES\n')
                planeta_seleccion = self.buscar_planeta()
                if planeta_seleccion is not None:
                    if planeta_seleccion.id != mision.destination.id:
                        mision.destination = planeta_seleccion
                        print('Planeta modificado...\n')
                        print(mision.show())
                    else:
                        print('El planeta ya se encuentra seleccionado...\n')
                else:
                    print('Planeta no encontrado...\n')

            elif opcion == "5":
                break

    def menu_misiones(self):
        """
        Menú de misiones. Muestra las diferentes acciones que se pueden realizar con las misiones.
        """
        print('\n- BIENVENIDO AL MENÚ DE MISIONES -')
        archivo = Archivo()
        if archivo.archivo_existe() and len(self.misiones) == 0:
            ans = input('Existe un archivo con misiones guardadas.\n¿Desea cargarlas? No podrá hacerlo luego. [y/n]: ')
            while ans.lower() not in ['y','n']:
                ans = input('Error...\n¿Desea cargarlas? [y/n]: ')
            if ans.lower() == 'y':
                self.txt_a_mision()
                print('Misiones cargadas...\n')

        while True:
            opcion = input('''
OPCIONES DE MISIONES
1. Construir una Misión
2. Modificar Misiones Creadas
3. Visualizar Misiones
4. Guardar Misiones Creadas
5. Volver
Ingrese el número correspondiente a su selección -> ''')
        
            match opcion:
                case "1": # Construir una misión
                    if len(self.misiones) != 5:

                        id = len(self.misiones) + 1
                        print('\nNOMBRE DE LA MISIÓN')
                        nombre = input('Ingrese el nombre de la misión -> ')


                        print('\nDESTINO DE LA MISIÓN')
                        destino = self.buscar_planeta()
                        if destino is None:
                            print('Misión cancelada...\n')
                            break

                        print('\nNAVE A UTILIZAR')
                        nave = self.buscar_nave()
                        if nave is None:
                            print('Misión cancelada...\n')
                            break


                        print('\nARMAS A UTILIZAR')
                        print('Puedes escoger hasta 7 armas...')
                        armas = []
                        while True:
                            arma = self.buscar_arma(armas)

                            if arma is None:
                                print('Arma no encontrada...\n')
                                if len(armas) == 0:
                                    print('Misión cancelada...\n')
                                    break
                            else:
                                if arma not in armas:
                                    armas.append(arma)
                                    print('Arma agregada...\n')
                                else:
                                    print('El arma ya se encuentra agregada...\n')
                                if len(armas) != 7:
                                    ans = input('¿Desea agregar otra arma? [y/n] -> ')
                                    while ans.lower() not in ['y','n']:
                                        ans = input('Error...\n¿Desea agregar otra arma? [y/n] -> ')
                                    if ans.lower() == 'n':
                                        break
                                else:
                                    break


                        print('\nINTEGRANTES DE LA MISIÓN')
                        print('Puedes escoger hasta 7 personajes...')
                        personajes = []
                        while True:
                            personaje = self.buscar_personajes2(personajes)

                            if personaje is None:
                                print('Personaje no encontrado...\n')
                                if len(personajes) == 0:
                                    print('Misión cancelada...\n')
                                    break
                            else:
                                if personaje not in personajes:
                                    personajes.append(personaje)
                                    print('Personaje agregado...\n')
                                else:
                                    print('El personaje ya se encuentra agregado...\n')
                                if len(personajes) != 7:
                                    ans = input('¿Desea agregar otro personaje? [y/n] -> ')
                                    while ans.lower() not in ['y','n']:
                                        ans = input('Error...\n¿Desea agregar otro personaje? [y/n] -> ')
                                    if ans.lower() == 'n':
                                        break
                                else:
                                    break
                        
                        self.misiones.append(Mision(id,nombre,destino,nave,armas,personajes))

                        print(f'¡Misión creada exitosamente!\nVisualice los detalles:\n{self.misiones[-1].show()}')
                    
                    else:
                        print('No puedes crear más misiones...\n')
                
                case "2": # Modificar misiones
                    if len(self.misiones) != 0:
                        print('MISIONES ACTUALES\n')
                        for i,mision in enumerate(self.misiones):
                            print(f'{mision.show()}')
                        
                        option = input("Ingrese el número correspondiente a la misión a modificar. [Ingrese 0 para volver al menú] --> ")
                        while not option.isnumeric() or int(option) > len(self.misiones) + 1:
                            option = input('Error...\nIngrese el número correspondiente a la misión a modificar. [Ingrese 0 para volver al menú] --> ')
                        
                        if option != "0":
                            mision_seleccion = self.buscar_objeto(int(option), self.misiones)
                            while mision_seleccion is None:
                                print('Misión no encontrada...\n')
                                option = input("Ingrese el número correspondiente a la misión a modificar. [Ingrese 0 para volver al menú] --> ")
                                mision_seleccion = self.buscar_objeto(option, self.misiones)

                            self.modificar_mision(mision_seleccion)

                            
                    else:
                        print('\nNo hay misiones creadas...\n')
                
                case "3": # Visualizar misiones
                    if len(self.misiones) != 0:
                        while True:
                            print('MISIONES ACTUALES\n')
                            for mision in self.misiones:
                                print(f'ID - {mision.id}. NOMBRE: {mision.name}')
                            mision_id = input('Ingrese el ID de la misión a visualizar -> ')

                            while not mision_id.isnumeric() or int(mision_id) > len(self.misiones) + 1:
                                mision_id = input('Error...\nIngrese el ID de la misión a visualizar -> ')

                            self.datos_mision(mision)
                            ans = input('¿Desea visualizar otra misión? [y/n] --> ')
                            while ans.lower() not in ['y','n']:
                                ans = input('Error...\n¿Desea visualizar otra misión? [y/n] --> ')
                            if ans.lower() == 'n':
                                break
                            
                    else:
                        print('\nNo hay misiones creadas...\n')
                
                case "4": # Guardar misiones
                    if len(self.misiones) != 0:
                        for mision in self.misiones:
                            print(mision.show())

                        opcion = input('¿Desea guardar las misiones creadas? Sobreescribirá el archivo si ya existente [y/n] --> ')
                        while opcion.lower() not in ['y','n']:
                            opcion = input('Error...\n¿Desea guardar las misiones creadas? [y/n] --> ')

                        if opcion.lower() == 'y':
                            print('Guardando misiones...')
                            self.mision_a_txt()
                            print('Misiones guardadas...\n')
                            self.continuar()
                        else:
                            print('Misiones no guardadas...\n')
                            self.continuar()
                    else:
                        print('\nNo hay misiones creadas...\n')
    
                case "5":
                    break
                case _:
                    print("Opción inválida.\n")


    # FUNCIONES DE ESTADISTICAS
    def menu_graficos(self):
        """
        Menú de gráficos. Presenta las distintas opciones de los gráficos
        """
        while True:
            print('\nGRÁFICOS\n')
            opcion = input('''¿Qué desea visualizar?
1. Características de las Naves
2. Cantidad de Personajes Nacidos en Planetas de la Saga
3. Volver
Ingrese el número de su selección --> ''')
            
            # Validación de la opción
            while not opcion.isnumeric() or int(opcion) not in range(1,4):
                opcion = input('Error...\nIngrese el número de su selección --> ')

            if opcion == "1": # GRÁFICOS DE LAS NAVES
                while True:
                    opcion_naves = input('''
¿Qué gráfico deseas visualizar?
1. Longitud de la Nave
2. Capacidad de Carga
3. Clasificación de hiperimpulsor
4. MGLT (Modern Galactic Light Time)
5. Volver
--> ''')
                    while not opcion_naves.isnumeric() or int(opcion_naves) not in range(1,6):
                        opcion_naves = input('Error...\n¿Qué gráfico deseas visualizar? --> ')

                    if opcion_naves == "1": # LONGITUD DE LAS NAVES

                        diccionario_longitud = {"unknown": 0} # Diccionario para almacenar la longitud de las naves
                        
                        for nave in self.naves:
                            if str(nave.length) not in diccionario_longitud:
                                diccionario_longitud[str(nave.length)] = 1 # Si no existe la longitud, se agrega al diccionario
                            else:
                                diccionario_longitud[str(nave.length)] += 1 # Si existe, se suma 1 a la cantidad de naves con esa longitud

                        # Genera 2 listas, una con las claves y otra con los valores
                        longitudes = list(diccionario_longitud.keys())
                        cantidad_longitudes = list(diccionario_longitud.values())

                        # Crear gráfico
                        plt.figure(figsize=(12,6)) # Establece el tamaño del gráfico
                        plt.bar(longitudes, cantidad_longitudes, color='purple') # Establece los valores de las barras y el color
                        plt.xlabel('Longitudes') # Establece el nombre del eje x
                        plt.ylabel('Cantidad de Naves con Longitud Específica') # Establece el nombre del eje y
                        plt.title('Longitud de la Nave') # Establece el título del gráfico
                        plt.xticks(rotation=90) # Rota los nombres del eje x
                        plt.tight_layout() # Ajusta el gráfico
                        plt.show() # Muestra el gráfico

                    elif opcion_naves == "2": # CAPACIDAD DE CARGA
                        diccionario_capacidad_carga = {"unknown": 0}
                        for nave in self.naves:
                            if str(nave.cargo_capacity) not in diccionario_capacidad_carga:
                                diccionario_capacidad_carga[str(nave.cargo_capacity)] = 1
                            else:
                                diccionario_capacidad_carga[str(nave.cargo_capacity)] += 1

                        capacidades = list(diccionario_capacidad_carga.keys())
                        cantidad_capacidades = list(diccionario_capacidad_carga.values())

                        plt.figure(figsize=(12,6))
                        plt.bar(capacidades, cantidad_capacidades, color='purple')
                        plt.xlabel('Capacidades')
                        plt.ylabel('Cantidad de Naves con Capacidad de Carga Específica')
                        plt.title('Capacidad de Carga')
                        plt.xticks(rotation=90)
                        plt.tight_layout()
                        plt.show()
                    
                    elif opcion_naves == "3": # HIPERIMPULSOR
                        diccionario_hiperimpulsor = {"unknown": 0}
                        for nave in self.naves:
                            if nave.hyperdrive_rating not in diccionario_hiperimpulsor:
                                diccionario_hiperimpulsor[str(nave.hyperdrive_rating)] = 1
                            else:
                                diccionario_hiperimpulsor[str(nave.hyperdrive_rating)] += 1

                        hiperimpulsor = list(diccionario_hiperimpulsor.keys())
                        cantidad_hiperimpulsor = list(diccionario_hiperimpulsor.values())

                        plt.figure(figsize=(12,6))
                        plt.bar(hiperimpulsor, cantidad_hiperimpulsor, color='purple')
                        plt.xlabel('Hiperimpulsores')
                        plt.ylabel('Cantidad de Naves con Hiperimpulsor Específico')
                        plt.title('Clasificación de Hiperimpulsor')
                        plt.xticks(rotation=90)
                        plt.tight_layout()
                        plt.show()
                    
                    elif opcion_naves == "4": # MGLT
                        diccionario_MGLT = {"unknown": 0}
                        for nave in self.naves:
                            if nave.MGLT not in diccionario_MGLT:
                                diccionario_MGLT[nave.MGLT] = 1
                            else:
                                diccionario_MGLT[nave.MGLT] += 1

                        MGLT = list(diccionario_MGLT.keys())
                        cantidad_MGLT = list(diccionario_MGLT.values())

                        plt.figure(figsize=(12,6))
                        plt.bar(MGLT, cantidad_MGLT, color='purple')
                        plt.xlabel('MGLT')
                        plt.ylabel('Cantidad de Naves con MGLT Específico')
                        plt.title('MGLT (Modern Galactic Light Time)')
                        plt.xticks(rotation=90)
                        plt.tight_layout()
                        plt.show()
                    else:
                        break

            elif opcion == "2": # GRÁFICO DE PERSONAJES EN PLANETAS
                # Planetas con episodios
                diccionario_planetas = {"unknown": 0}

                for planeta in self.planetas:
                    if len(planeta.films) > 0: # Si el planeta tiene episodios (sale en la saga)
                        if len(planeta.residents) > 0: # Si se conoce la cantidad de residentes
                            diccionario_planetas[planeta.name.capitalize().strip()] = len(planeta.residents)
                        else: # Si se desconoce la cantidad de residentes
                            diccionario_planetas["unknown"] += 1
                # Crear gráfico
                nombres_planetas = list(diccionario_planetas.keys())
                cantidad_personajes = list(diccionario_planetas.values())

                plt.figure(figsize=(10,5))
                plt.bar(nombres_planetas, cantidad_personajes, color='purple')
                plt.xlabel('Planetas')
                plt.ylabel('Cantidad de Personajes')
                plt.title('Cantidad de Personajes Nacidos en Planetas de la Saga')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()
            else:
                break

    def menu_estadisticas(self):
        """
        Estadísticas de las clases de nave
        """
        print('\nTABLA DE ESTADÍSTICOS BÁSICOS DE LAS NAVES\n')
        clases_de_naves = {}
        funciones_estadisticas = Estadistica()
        # Guarda las clase de las naves con sus respectivas estadísticas
        for nave in self.naves:
            if nave.starship_class.capitalize().strip() not in clases_de_naves:
                clases_de_naves[nave.starship_class.capitalize().strip()] = {
                    "hyperdrive_rating": [],
                    "MGLT": [],
                    "max_atmosphering_speed": [],
                    "cost_in_credits": []
                }
        
            # Guarda las estadísticas de cada nave por clase
            #   - hyperdrive_rating
            if nave.hyperdrive_rating is not None and funciones_estadisticas.is_number(nave.hyperdrive_rating):
                clases_de_naves[nave.starship_class.capitalize().strip()]["hyperdrive_rating"].append(float(nave.hyperdrive_rating))
            
            #   - MGLT
            if nave.MGLT is not None and funciones_estadisticas.is_number(nave.MGLT):
                clases_de_naves[nave.starship_class.capitalize().strip()]["MGLT"].append(float(nave.MGLT))
            
            #  - max_atmosphering_speed
            if nave.max_atmosphering_speed is not None and funciones_estadisticas.is_number(nave.max_atmosphering_speed):
                clases_de_naves[nave.starship_class.capitalize().strip()]["max_atmosphering_speed"].append(float(nave.max_atmosphering_speed))

            #  - cost_in_credits
            if nave.cost_in_credits is not None and funciones_estadisticas.is_number(nave.cost_in_credits):
                clases_de_naves[nave.starship_class.capitalize().strip()]["cost_in_credits"].append(float(nave.cost_in_credits))

        # Encabezado de la tabla
        print(f"{'Clase de Nave':<32}|{'Variable':<25}|{'Promedio':<15}|{'Moda':<15}|{'Máximo':<15}|{'Mínimo':<15}")
        print("-"*150)

        # Accede a cada clase dentro del diccionario
        for clase, data in clases_de_naves.items():
            # Accede a los datos de la clase de nave
            #   Calcula cada estadístico por variable
            for variable, values in data.items():
                promedio = funciones_estadisticas.calcular_promedio(values)
                moda = funciones_estadisticas.calcular_moda(values)
                maximo = funciones_estadisticas.valor_maximo(values)
                minimo = funciones_estadisticas.valor_minimo(values)
                if promedio != None:
                    promedio_str = f"{promedio:<15.2f}"
                else:
                    promedio_str = f"{'?':<15}"

                if moda != None:
                    moda_str = f"{moda:<15.2f}"
                else:
                    moda_str = f"{'?':<15}"
                
                if maximo != None:
                    maximo_str = f"{maximo:<15.2f}"
                else:
                    maximo_str = f"{'?':<15}"

                if minimo != None:
                    minimo_str = f"{minimo:<15.2f}"
                else:
                    minimo_str = f"{'?':<15}"

                print(f"{clase:<32} | {variable:<25} | {promedio_str} | {moda_str} | {maximo_str} | {minimo_str}")

    # FUNCIONES DE SALIDA / ESTÉTICA
    def exit(self):
        """
        Mensaje de salida.
        """
        print("Gracias por su visita, vuelva pronto...")

    def continuar(self):
        """
        Pausa en la ejecución del programa. Limpia la pantalla luego de que el usuario presione la tecla indicada.
        Función auxiliar para mejorar la experiencia del usuario.
        """
        input('Presione ENTER para continuar...\n')
        os.system('cls' if os.name == 'nt' else 'clear')


    # MENU INICIAL
    def menu(self):
        """
        Menu inicial del sistema.
        """
        self.get_api_info()
        
        print('''STAR WARS METROPEDIA
- "Que la fuerza te acompañe" -
Bienvenido/a''')
        
        while True:
            option = input('''
MENÚ 
1. Ver Películas de la Saga
2. Ver Especies de Seres Vivos
3. Ver Planetas
4. Buscar Personajes
---------------------
5. Visualizar Gráficos
6. Estadísticas sobre Naves
---------------------
7. Misiones
---------------------
8. Salir

Ingrese el número correspondiente a su selección -> ''')
            match option:
                case "1":
                    print('PELICULAS\n')
                    self.mostrar_peliculas()
                    self.continuar()
                case "2":
                    print("ESPECIES\n")
                    self.mostrar_especies()
                    self.continuar()
                case "3":
                    print("PLANETAS\n")
                    self.mostrar_planetas()
                    self.continuar()
                case "4":
                    self.buscar_personajes()
                case "5":
                    self.menu_graficos()
                    self.continuar()
                case "6":
                    self.menu_estadisticas()
                    self.continuar()
                case "7":
                    self.menu_misiones()
                case "8":
                    self.exit()
                    break
                case _:
                    print("OPCIÓN INVÁLIDA... Intente nuevamente\n")

    # MAIN
def main():
    app = App()
    app.menu()

main()
