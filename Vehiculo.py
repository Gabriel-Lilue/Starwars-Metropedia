from Transporte import Transporte

class Vehiculo(Transporte):
    def __init__(self, id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,cargo_capacity,vehicle_class):
        """
        Constructor de la clase Vehiculo. Hereda de la clase Transporte

        Args:
            id (int): ID del transporte
            name (string): Nombre del transporte
            model (string): Modelo l transporte
            manufacturer (string): Fabricante del transporte
            cost_in_credits (float): Costo en créditos del transporte
            length (float): Longitud del transporte
            max_atmosphering_speed (float): Velocidad máxima en la atmósfera del transporte
            cargo_capacity (float): Capacidad de carga del transporte
            vehicle_class (string): Clase del Vehiculo
        """
        super().__init__(id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,cargo_capacity)
        self.vehicle_class = vehicle_class

    def show(self):
        """
        Metodo para mostrar las variables de manera amigable
        Returns:
            string: Mensaje con las variables del objeto
        """
        return f'''{super().show()}
CLASE: {self.vehicle_class}'''