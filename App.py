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

    # CENTRALIZAR FUNCIONES DE LA API
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
        self.csv_info() # Aqui actualizar las listas de objetos y agregar armas
        print('Información actualizada...')
        self.continuar()
    

    # FUNCIONES UTILES
    def add_URLs(self, name, url):
        self.urls[name] = url
    
    def find_URLs_match(self, url):
        for name, url_match in self.urls.items():
            if url_match == url:
                return name
        return None
            
    def return_list(self, lista):
        if len(lista) != 0:
            for url in lista:
                name = self.find_URLs_match(url)
                if name is not None:
                    lista[lista.index(url)] = name
        return lista

    def get_all_items(self, url):
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
        for elemento in lista:
            if int(elemento.id) == id:
                print('a')
                return elemento
        return None
    
    def buscar_objeto2(self, name, lista):
        for elemento in lista:
            if elemento.name == name:
                print('a')
                return elemento
        return None

    # OBTENER INFORMACION DE LA API
    def get_transporte(self):
        url = 'https://swapi.dev/api/vehicles/'
        vehiculos = self.get_all_items(url) # Obtenemos todos los vehiculos de la API
        # self, id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,cargo_capacity,vehicle_class):
        for vehiculo in vehiculos:
            id = len(self.vehiculos) + 1
            name = vehiculo['name']
            model = vehiculo['model']
            manufacturer = vehiculo['manufacturer']
            cost_in_credits = vehiculo['cost_in_credits']
            length = vehiculo['length']
            max_atmosphering_speed = vehiculo['max_atmosphering_speed']
            cargo_capacity = vehiculo['cargo_capacity']
            vehicle_class = vehiculo['vehicle_class']

            self.add_URLs(name, vehiculo['url'])

            self.vehiculos.append(Vehiculo(id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,cargo_capacity,vehicle_class))

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
            
            # self, id, episode_id, release_date, opening_crawl, director, producer
            self.peliculas.append(Pelicula(id,title,episode_id,release_date ,opening_crawl,director,producer))

    def get_especies(self):
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
        # Aqui se agregan las armas
        archivo = Archivo()
        armas = archivo.leer_csv('csv/weapons.csv')
        for arma in armas:
            # id,name,model,manufacturer,cost_in_credits ,length ,type,description,films

            # id,name,model,manufacturer,cost_in_credits,length,type,description,films
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
                
                if "," in planeta_csv[11]:
                    films = planeta_csv[11].split(",")
                else:
                    [planeta_csv[11]]

                self.planetas.append(Planeta(id,name,diameter,rotation_period,orbital_period,gravity,population,climate,terrain,surface_water,residents,films))

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
                # id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,cargo_capacity,hyperdrive_rating,MGLT,starship_class
                # id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,crew,passengers,cargo_capacity,consumables,hyperdrive_rating,MGLT,starship_class,pilots,films
                name = nave_csv[1]
                model = nave_csv[2]
                manufacturer = nave_csv[3]
                cost_in_credits = nave_csv[4]
                length = nave_csv[5]
                max_atmosphering_speed = nave_csv[6]
                cargo_capacity = nave_csv[9]
                hyperdrive_rating = nave_csv[11]
                MGLT = nave_csv[12]
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
                # id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,cargo_capacity,vehicle_class
                # id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,crew,passengers,cargo_capacity,consumables,vehicle_class,pilots,films
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
        for arma in self.armas:
            print(arma.show())
    
    def mostrar_personajes(self):
        for personaje in self.personajes:
            print(personaje.show())

    def mostrar_peliculas(self):
        for pelicula in self.peliculas:
            print(pelicula.show())

    def mostrar_especies(self):
        for especie in self.especies:
            print(especie.show())

    def mostrar_planetas(self):
        for planeta in self.planetas:
            print(planeta.show())

    def mostrar_naves(self):
        for nave in self.naves:
            print(nave.show())

    # FUNCIONES DE BUSCAR
    def buscar_personajes(self):
        while True:
            print('\nBÚSQUEDA DE PERSONAJES')
            name = input('Ingrese el nombre del personaje deseado -> ').lower()

            results = []
            for personaje in self.personajes:
                if name in personaje.name.lower():
                    results.append(personaje)

            if len(results) == 0:
                ans = input('No hay coincidencias.\n¿Desea reintentar? [y/n] --> ')
                while ans.lower() not in ['y','n']:
                    ans = input('Error...\n¿Desea reintentar? [y/n] --> ')
                if ans.lower() == 'n':
                    break
            else:
                print('\nSe han encontrado las siguientes coincidencias:\n')
                for p in results:
                    print(p.show())

                ans = input('¿Desea buscar otro personaje? [y/n] --> ')
                while ans.lower() not in ['y','n']:
                    ans = input('Error...\n¿Desea buscar otro personaje? [y/n] --> ')
                if ans.lower() == 'n':
                    break

    def buscar_personajes2(self, lista_personaes):
        for personaje in self.personajes:
            if personaje not in lista_personaes:
                print(personaje.show())

        while True:
            personaje_seleccion = input('Ingrese el ID del personaje deseado -> ')

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
    # Eduardo
    def txt_a_mision(self):
        lista_misiones_txt = Archivo().acceder_data()
        if lista_misiones_txt[len(lista_misiones_txt) - 1] == "":
            lista_misiones_txt.pop()

        for mision_txt in lista_misiones_txt:
            mision = mision_txt.split(",")
            id = int(mision[0])
            name = mision[1]
            destination = self.buscar_objeto2(mision[2], self.planetas)
            spaceship = self.buscar_objeto2(mision[3], self.naves)

            weapons_txt = mision[4].split("---")
            weapons = []
            for weapon in weapons_txt:
                arma = self.buscar_objeto2(weapon, self.armas)
                if arma is not None:
                    weapons.append(arma)

            characters_txt = mision[5].split("---")
            characters = []
            for character in characters_txt:
                personaje = self.buscar_objeto2(character, self.personajes)
                if personaje is not None:
                    characters.append(personaje)

            self.misiones.append(Mision(id,name,destination,spaceship,weapons,characters))
            print(Mision(id,name,destination,spaceship,weapons,characters).show())

    def mision_a_txt(self):
        misiones_txt = ""
        archivo = Archivo()

        for mision in self.misiones:
            mision_string = ""

            mision_string += f"{mision.id},{mision.name},{mision.destination.name},{mision.spaceship.name},{archivo.listoToString(mision.weapons)},{archivo.listoToString(mision.characters)}"
            # mision_string += archivo.listoToString(mision.weapons)
            # mision_string += archivo.listoToString(mision.characters)
            misiones_txt += mision_string + "\n"

        archivo.guardar_data(misiones_txt)
        
    def datos_mision(self,mision):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(mision.show())
        print('Datos Específicos')
        mision.show_destination()
        mision.show_spaceship()
        mision.show_weapons()
        mision.show_characters()
    
    def modificar_mision(self,mision):
        print('\nMODIFICAR MISIÓN\n')
        print(mision.show())

        while True:
            opcion = input('''¿Qué deseas modificar?
1. Armas a Utilizar
2. Integrantes de la Misión
3. Volver
--> ''')
            while not opcion.isnumeric() or int(opcion) not in [1,2,3]:
                opcion = input('Error...\n¿Qué deseas modificar? --> ')

            if opcion == "1": # ARMAS
                opcion_armas = input('\nMODIFICAR ARMAS\n1. Agregar\n2. Eliminar\n3. Volver\n--> ')
                while not opcion_armas.isnumeric() or int(opcion_armas) not in [1,2,3]:
                    opcion_armas = input('Error...\n¿Qué deseas hacer? --> ')
                
                if opcion_armas == "1": # AGREGAR
                    if len(mision.weapons) != 7:
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
                    if len(mision.weapons) != 0:
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
                        print('No hay armas para eliminar...\n')
                
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
                    if len(mision.characters) != 0:
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
                        print('No hay personajes para eliminar...\n')
                
            elif opcion == "3":
                break

    def menu_misiones(self):
        print('- BIENVENIDO AL MENÚ DE MISIONES -')
        archivo = Archivo()
        if archivo.archivo_existe() and len(self.misiones) != 0:
            ans = input('Existe un archivo con misiones guardadas.\n¿Desea cargarlas? No podrá hacerlo luego. [y/n]: ')
            while ans.lower() not in ['y','n']:
                ans = input('Error...\n¿Desea cargarlas? [y/n]: ')
            if ans.lower() == 'y':
                self.txt_a_mision()
                print('Misiones cargadas...\n')

        while True:
            opcion = input('''
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
                
                case "2": # Modificar misiones (FALTA)
                    if len(self.misiones) != 0:
                        print('MISIONES ACTUALES\n')
                        for i,mision in enumerate(self.misiones):
                            print(f'{mision.show()}')
                        
                        option = input("Ingrese el número correspondiente a la misión a modificar. [Ingrese 0 para volver al menú] --> ")
                        while not option.isnumeric() or int(option) > len(self.misiones) + 1:
                            option = input('Error...\nIngrese el número correspondiente a la misión a modificar. [Ingrese 0 para volver al menú] --> ')
                        
                        mision_seleccion = self.buscar_objeto(int(option), self.misiones)
                        while mision_seleccion is None:
                            print('Misión no encontrada...\n')
                            option = input("Ingrese el número correspondiente a la misión a modificar. [Ingrese 0 para volver al menú] --> ")
                            mision_seleccion = self.buscar_objeto(option, self.misiones)
                        
                        self.modificar_mision(mision_seleccion)

                        if option != '0':
                            pass
                            
                    else:
                        print('No hay misiones creadas...\n')
                
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
                        print('No hay misiones creadas...\n')
                
                case "4": # Guardar misiones
                    for mision in self.misiones:
                        print(mision.show())
                    
                    opcion = input('¿Desea guardar las misiones creadas? Sobreescribirá el archivo ya existente [y/n] --> ')
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
    
                case "5":
                    break
                case _:
                    print("Opción inválida.\n")


    # FUNCIONES DE ESTADISTICAS
    # Santiago
    def graficos(self):
        pass

    def estadisticas(self):
        pass


    def exit(self):
        # aqui crear funcion para guardar info de txt
        print("Gracias por su visita, vuelva pronto...")

    def continuar(self):
        input('Presione ENTER para continuar...\n')
        os.system('cls' if os.name == 'nt' else 'clear')



    def menu(self):
        self.get_api_info()

        print('''STAR WARS METROPEDIA
- "Que la fuerza te acompañe" -
Bienvenido/a''')
        
        while True:
            option = input(''' MENÚ 
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
                    for nave in self.naves:
                        print(nave.show())
                case "6":
                    self.estadisticas()
                case "7":
                    self.menu_misiones()
                case "8":
                    self.exit()
                    break
                case _:
                    print("OPCIÓN INVÁLIDA... Intente nuevamente\n")

def main():
    app = App()
    app.menu()

main()
