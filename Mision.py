class Mision:
    def __init__(self, id,name, destination, spaceship, weapons, characters):
        self.id = id
        self.name = name
        self.destination = destination
        self.spaceship = spaceship
        self.weapons = weapons
        self.characters = characters

    def show(self):
        return f'''{self.id} - INFORMACIÓN DE LA MISIÓN - 
NOMBRE: {self.name}
PLANETA DESTINO: {self.destination.name}
ARMAS:
{self.show_array(self.weapons)}
INTEGRANTES:
{self.show_array(self.characters)}
'''
    
    def show_array(self,lista):
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
    
    def show_array2(self,lista):
        pass

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