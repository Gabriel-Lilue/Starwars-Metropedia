from Transporte import Transporte

class Nave(Transporte):
    def __init__(self, id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,cargo_capacity,hyperdrive_rating,MGLT,starship_class):
        super().__init__(id,name,model,manufacturer,cost_in_credits,length,max_atmosphering_speed,cargo_capacity)
        self.hyperdrive_rating = hyperdrive_rating
        self.MGLT = MGLT
        self.starship_class = starship_class

    def show(self):
        return f'''{super().show()}HIPERDRIVE: {self.hyperdrive_rating}
MGLT: {self.MGLT}
CLASE: {self.starship_class}
'''