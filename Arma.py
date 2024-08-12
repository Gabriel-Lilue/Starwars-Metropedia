class Arma:
    def __init__(self, id,name,model,manufacturer,cost_in_credits ,length ,weapon_type,description,films):
        """
        Constructor de la clase Arma
        Args:
            id (int): ID del arma
            name (string): Nombre del arma
            model (string): Modelo del arma
            manufacturer (string): Fabricante del arma
            cost_in_credits (float): Costo en creditos del arma
            length (float): Longitud del arma
            weapon_type (string): Tipo de arma
            description (string): Descripcion del arma
            films (string): Peliculas en las que aparece el arma
        """
        self.id = id
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.weapon_type = weapon_type
        self.description = description
        self.films = films

    def show(self):
        """
        Metodo para mostrar las variables de manera amigable
        Returns:
            string: Mensaje con las variables del objeto
        """
        return f'''ID {self.id}. --------
NOMBRE: {self.name} - MODELO: {self.model} - FABRICANTE: {self.manufacturer}
TIPO: {self.weapon_type} - COSTO EN CREDITOS: {self.cost_in_credits} - LONGITUD: {self.length}
DESCRIPCION: {self.description}
PELICULAS: {self.films}
'''