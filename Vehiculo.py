from Transporte import Transporte

class Vehiculo(Transporte):
    def __init__(self, id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,cargo_capacity,vehicle_class):
        super().__init__(id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,cargo_capacity)
        self.vehicle_class = vehicle_class

    def show(self):
        return f'''{super().show()}
CLASE: {self.vehicle_class}'''