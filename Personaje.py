class Personaje:
    # Constructor
    def __init__(self, id, name, species, gender, films, homeworld, starships, vehicles):
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
        return f'''{self.id}. --------
NOMBRE: {self.name} - GENERO: {self.gender} - PLANETA DE ORIGEN: {self.homeworld}
EPISODIOS: {self.show_array2(self.films)}
ESPECIE: {self.species}
NAVES: {self.show_array(self.starships)}
VEHICULOS: {self.show_array(self.vehicles)}
'''
    
    # Método para mostrar los elementos de una lista
    def show_array(self,lista):
        msg = ''
        if len(lista) == 0:
            return 'No especificado'
        else:
            for element in lista:
                msg += f'{element}\n'
            return msg
    
    def show_array2(self,lista):
        msg = ''
        for i,element in enumerate(lista):
            if i != len(lista)-1:
                msg += f'{element}, '
            else:
                msg += f'{element}'
        return msg