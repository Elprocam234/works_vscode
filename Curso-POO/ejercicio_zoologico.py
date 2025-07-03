

class Animal:   
    def comer(self): 
        print("Animal esta comiendo")

class Mamifero(Animal):
    def amamantar(self):
        print("esta amamantando")

class Ave(Animal):
    def volar(self):
        print("Esta volando")

class Murcielago(Mamifero,Ave):
    pass

Animal_1 = Murcielago()

# Tomamos como referencia el objeto murcielo, para imprimir el metodo amamantar que esta en mamifero 
Mamifero.amamantar(Murcielago)

