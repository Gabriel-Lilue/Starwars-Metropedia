class Planeta:
    def __init__(self, id,name,diameter,rotation_period,orbital_period,gravity,population,climate,terrain,surface_water,residents,films) :
        self.id = id 
        self.name = name 
        self.diameter = diameter
        self.rotation_period = rotation_period
        self.orbital_period = orbital_period
        self.gravity = gravity
        self.population = population
        self.climate = climate
        self.terrain = terrain
        self.surface_water = surface_water
        self.residents = residents
        self.films = films


    # Para mostrar las variables de manera amigable
    def show(self):
        return f'''{self.id}. --------
NOMBRE: {self.name}
PERIODO DE ORBITA: {self.orbital_period} - PERIODO DE ROTACION: {self.rotation_period}
CANTIDAD DE HABITANTES: {self.population} - TIPO DE CLIMA: {self.climate}
RESIDENTES:
{self.show_array2(self.residents)}
EPISODIOS:
{self.show_array2(self.films)}
'''
    def show_array(self,lista):
        msg = ''
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
                    msg += f'{element.strip()}, '
                else:
                    msg += f'{element.strip()}'
            return msg