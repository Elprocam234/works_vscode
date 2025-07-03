
class TanqueCombustible: 
    def __init__(self):
        self.combustible  = 100 
    def agregar_combustible(self, cantidad):
        self.combustible  += cantidad
    def obtener_combustible(self):
        return self.combustible
    def usar_combustible(self,cantidad): 
        self.combustible -= cantidad 
    def cantidad_combustible_necesario(self,cantidad):
        combustible_necesario = cantidad - self.combustible
        print(f"actualmente tienes {self.combustible} y necesitas {combustible_necesario} ")
    

class Auto: 
    def __init__(self,tanque):
        self.posicion = 0
        self.tanque = tanque
    
    def mover(self, distancia): 
        if self.tanque.obtener_combustible() >= distancia / 2 : 
            self.posicion += distancia 
            self.tanque.usar_combustible(distancia / 2 )
            print("Haz movido el carro exitosamente")
        else: 
            return self.tanque.cantidad_combustible_necesario(distancia/2)


    def obtener_posicion(self):
        return self.posicion
    



tanque = TanqueCombustible()
auto1 = Auto(tanque)


print(auto1.obtener_posicion())
auto1.mover(10)
print(auto1.obtener_posicion())
auto1.mover(10)
print(auto1.obtener_posicion())
auto1.mover(10)
print(auto1.obtener_posicion())
auto1.mover(200)

