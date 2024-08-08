class Especie:
    def __init__(self, id, name, classification, designation, average_height, skin_colors, hair_colors, eye_colors, average_lifespan, language, homeworld, people, films):
        self.id = id
        self.name = name
        self.classification = classification
        self.designation = designation
        self.average_height = average_height
        self.skin_colors = skin_colors
        self.hair_colors = hair_colors
        self.eye_colors = eye_colors
        self.average_lifespan = average_lifespan
        self.language = language
        self.homeworld = homeworld
        self.people = people
        self.films = films

# Para mostrar las variables de manera amigable
    def show(self):
        return f'''{self.id}. --------
NOMBRE: {self.name} - ESTATURA: {self.average_height} - CLASIFICACIÓN: {self.classification}
PLANETA DE ORIGEN: {self.homeworld} - LENGUA MATERNA: {self.language}
PERSONAJES:
{self.show_array(self.people)}
EPISODIOS:
{self.show_array(self.films)}
'''
    
    def show_array(self,lista):
        msg = ''
        for element in lista:
            msg += f'{element}\n'
        return msg