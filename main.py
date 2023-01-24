from pickle import dump, load


class Vehiculo:
    def __init__(self, velocidad, pasajeros, carga):
        self.velocidad = velocidad
        self.pasajeros = pasajeros
        self.carga = carga

    def __str__(self):
        return f'Velocidad: {self.velocidad} km/h; Pasajeros: {self.pasajeros}; Carga: {self.carga} kilogramos;'


f = open('vehiculo', 'wb')
dump(Vehiculo(120, 4, 1300), f)
f.close()

f = open('vehiculo', 'rb')
vehiculo = load(f)
f.close()
print(vehiculo)