


class Animal: 
    def __init__(self, nombre):
        self.nombre = nombre 
    
    def hacer_sonido(self):
        print("Hacer sonido")

class Perro(Animal):
    def __init__(self, nombre,raza):
        super().__init__(nombre)
        #self es una referencia a la instancia actual y .raza es un atributo de esa instancia
        self.raza = raza 
    def hacer_sonido(self):
        super().hacer_sonido()
        print("gua gua")
    
animal1 = Perro("Oscar", "Leopolo")
animal1.hacer_sonido()