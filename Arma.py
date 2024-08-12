class Arma:
    def __init__(self, id,name,model,manufacturer,cost_in_credits ,length ,weapon_type,description,films):
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
        return f'''ID {self.id}. --------
NOMBRE: {self.name} - MODELO: {self.model} - FABRICANTE: {self.manufacturer}
TIPO: {self.weapon_type} - COSTO EN CREDITOS: {self.cost_in_credits} - LONGITUD: {self.length}
DESCRIPCION: {self.description}
PELICULAS: {self.films}
'''