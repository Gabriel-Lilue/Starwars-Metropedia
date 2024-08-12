# CLASE PADRE

class Transporte:
    def __init__(self, id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,cargo_capacity):
        """
        Constructor de la clase Transporte. Clase padre de Vehiculo y Nave.

        Args:
            id (int): ID del transporte
            name (string): Nombre del transporte
            model (string): Modelo l transporte
            manufacturer (string): Fabricante del transporte
            cost_in_credits (float): Costo en créditos del transporte
            length (float): Longitud del transporte
            max_atmosphering_speed (float): Velocidad máxima en la atmósfera del transporte
            cargo_capacity (float): Capacidad de carga del transporte
        """
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
        """
        Metodo para mostrar las variables de manera amigable
        Returns:
            string: Mensaje con las variables del objeto
        """
        return f'''{self.id}. --------
NOMBRE: {self.name} - MODELO: {self.model} - FABRICANTE: {self.manufacturer}
COSTO EN CREDITOS: {self.cost_in_credits} - LONGITUD: {self.length}
VELOCIDAD MAXIMA: {self.max_atmosphering_speed} - CAPACIDAD DE CARGA: {self.cargo_capacity}
--------
'''