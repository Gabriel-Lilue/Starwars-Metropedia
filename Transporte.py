# CLASE PADRE

class Transporte:
    def __init__(self, id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,cargo_capacity):
        self.id = id
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.max_atmosphering_speed = max_atmosphering_speed
        self.cargo_capacity = cargo_capacity

    # Para mostrar las variables de manera amigable
    def show(self):
        return f'''{self.id}. --------
NOMBRE: {self.name} - MODELO: {self.model} - FABRICANTE: {self.manufacturer}
COSTO EN CREDITOS: {self.cost_in_credits} - LONGITUD: {self.length}
VELOCIDAD MAXIMA: {self.max_atmosphering_speed} - CAPACIDAD DE CARGA: {self.cargo_capacity}
--------
'''