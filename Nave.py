from Transporte import Transporte

class Nave(Transporte):
    def __init__(self, id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,cargo_capacity,hyperdrive_rating,MGLT,starship_class):
        """
        Constructor de la clase Nave. Hereda de Transporte
        Args:
            id (int): ID de la nave
            name (string): Nombre de la nave
            model (string): Modelo del nave
            manufacturer (string): Fabricante de la nave
            cost_in_credits (float): Costo en créditos de la nave
            length (float): Longitud de la nave
            max_atmosphering_speed (float): Velocidad máxima en la atmósfera de la nave
            cargo_capacity (float): Capacidad de carga de la nave
            hyperdrive_rating (float): Clasificación de hiperimpulsor
            MGLT (float): "Modern Galactic Light Time" de la nave
            starship_class (string): Clase de la nave
        """
        super().__init__(id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,cargo_capacity)
        self.hyperdrive_rating = hyperdrive_rating
        self.MGLT = MGLT
        self.starship_class = starship_class

    def show(self):
        """
        Metodo para mostrar las variables de manera amigable
        Returns:
            string: Mensaje con las variables del objeto
        """
        return f'''{super().show()}HIPERDRIVE: {self.hyperdrive_rating}
MGLT: {self.MGLT}
CLASE: {self.starship_class}
'''