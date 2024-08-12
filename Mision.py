class Mision:
    def __init__(self, id,name, destination, spaceship, weapons, characters):
        """
        Constructor de la clase Mision

        Args:
            id (int): ID de la misión
            name (string): Nombre de la misión
            destination (Planeta): Planeta destino
            spaceship (Nave): Nave a utilizar en la misión
            weapons (list[Arma]): Lista de objetos de tipo Arma
            characters (list[Personaje]): Lista de objetos de tipo Personaje
        """
        self.id = id
        self.name = name
        self.destination = destination
        self.spaceship = spaceship
        self.weapons = weapons
        self.characters = characters

    def show(self):
        """
        Metodo para mostrar las variables de manera amigable
        Returns:
            string: Mensaje con las variables del objeto
        """
        return f'''{self.id} - INFORMACIÓN DE LA MISIÓN - 
NOMBRE: {self.name}
PLANETA DESTINO: {self.destination.name}
NAVE: {self.spaceship.name}
ARMAS:
{self.show_array(self.weapons)}
INTEGRANTES:
{self.show_array(self.characters)}
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
            for i,element in enumerate(lista):
                if i != len(lista)-1:
                    msg += f'{element.name}, '
                else:
                    msg += f'{element.name}'
            return msg

    # FUNCIONES PARA MOSTRAR LA INFORMACIÓN DE CADA OBJETO
    def show_destination(self):
        print('DESTINO\n')
        print(self.destination.show())
    
    def show_spaceship(self):
        print('NAVE ESPACIAL\n')
        print(self.spaceship.show())
    
    def show_weapons(self):
        print('ARMAS\n')
        for weapon in self.weapons:
            print(weapon.show())

    def show_characters(self):
        print('INTEGRANTES\n')
        for character in self.characters:
            print(character.show())