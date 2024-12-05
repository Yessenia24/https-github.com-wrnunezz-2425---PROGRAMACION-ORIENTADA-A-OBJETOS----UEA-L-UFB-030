class Vehiculo:
    def mover(self):
        pass

class Carro(Vehiculo):
    def mover(self):
        return "El carro está conduciendo."

class Avion(Vehiculo):
    def mover(self):
        return "El avión está volando."

# Uso
vehiculos = [Carro(), Avion()]
for vehiculo in vehiculos:
    print(vehiculo.mover())