class Especie:
    def __init__(self, id, name, classification, designation, average_height, skin_colors, hair_colors, eye_colors, average_lifespan, language, homeworld, people, films):
        """
        Constructor de la clase Especie

        Args:
            id (int): ID de la especie
            name (string): Nombre de la especie
            classification (string): Clasificación de la especie
            designation (string): Designación de la especie
            average_height (float): Altura promedio de la especie
            skin_colors (string): Colores de piel de la especie
            hair_colors (string): Colores de cabello de la especie
            eye_colors (string): Colores de ojos de la especie
            average_lifespan (float): Esperanza de vida promedio de la especie
            language (string): Lengua materna de la especie
            homeworld (string): Planeta de orgien de la especie
            people (list): Lista de personajes de esta especie
            films (list): Lista de peliculas en la que aparece esta especie
        """
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
        """
        Metodo para mostrar las variables de manera amigable
        Returns:
            string: Mensaje con las variables del objeto
        """
        return f'''{self.id}. --------
NOMBRE: {self.name} - ESTATURA: {self.average_height} - CLASIFICACIÓN: {self.classification}
PLANETA DE ORIGEN: {self.homeworld} - LENGUA MATERNA: {self.language}
PERSONAJES:
{self.show_array(self.people)}
EPISODIOS:
{self.show_array(self.films)}
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
        for element in lista:
            msg += f'{element}\n'
        return msg