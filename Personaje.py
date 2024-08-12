class Personaje:
    def __init__(self, id, name, species, gender, films, homeworld, starships, vehicles):
        """
        Constructor de la clase Personaje
        Args:
            id (int): ID del personaje
            name (string): Nombre del personaje
            species (string): Especie del personaje
            gender (string): Género del personaje
            films (list): Lista con los episodios en los que aparece el personaje
            homeworld (string): Nombre del planeta de origen del personaje
            starships (list): Lista de naves que maneja el personaje
            vehicles (list): Lista de vehículos que maneja el personaje
        """
        self.id = id
        self.name = name
        self.species = species 
        self.gender = gender
        self.films = films 
        self.homeworld = homeworld
        self.starships = starships
        self.vehicles = vehicles

    # Para mostrar las variables de manera amigable
    def show(self):
        """
        Metodo para mostrar las variables de manera amigable
        Returns:
            string: Mensaje con las variables del objeto
        """
        return f'''{self.id}. --------
NOMBRE: {self.name} - GENERO: {self.gender} - PLANETA DE ORIGEN: {self.homeworld}
EPISODIOS: {self.show_array2(self.films)}
ESPECIE: {self.species}
NAVES: {self.show_array(self.starships)}
VEHICULOS: {self.show_array(self.vehicles)}
'''
    def show_array(self,lista):
        """
        Transforma una lista a string
        Args:
            lista (list): lista de elementos a colocar en un string
        Returns:
            string: mensaje con la información de los elementos de la lista
        """
        msg = ''
        if len(lista) == 0:
            return 'No especificado'
        else:
            for element in lista:
                msg += f'{element}\n'
            return msg
    
    def show_array2(self,lista):
        """
        Transforma una lista a string
        Args:
            lista (list): lista de elementos a colocar en un string
        Returns:
            string: mensaje con la información de los elementos de la lista
        """
        if len(lista) == 0:
            return 'No especificado'
        else:
            msg = ''
            for i,element in enumerate(lista):
                if i != len(lista)-1:
                    msg += f'{element}, '
                else:
                    msg += f'{element}'
            return msg