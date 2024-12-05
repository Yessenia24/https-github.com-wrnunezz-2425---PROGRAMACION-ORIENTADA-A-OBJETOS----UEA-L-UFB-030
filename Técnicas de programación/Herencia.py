# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

# Clases derivadas
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

# Uso
animales = [Perro("Max"), Gato("Luna")]
for animal in animales:
    print(f"{animal.nombre} dice: {animal.hacer_sonido()}")