from pprint import pprint


class Vehiculo:
    def __init__(self, color='', ruedas=0, puertas=0):
        super().__init__()
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):

    def __init__(self, color='blanco', ruedas=4, puertas=5, velocidad=120, cilindrada=100):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


pprint(Coche().__dict__)
