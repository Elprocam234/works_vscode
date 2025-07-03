#manejar la complejidad ocultado todos los datos innecesarios al programador 

class Auto: 
    #Atributos 
    def __init__(self):
        self._estado = "apagado"
    #metodos 
    def encender(self): 
        self._encender = "Encendido"
        print("El auto esta encendio")
    
    def conducir(self): 
        if self._estado == "apagado": 
            self.encender()
            print("el auto esta conduciendo ")
    
mi_auto = Auto()
# abstraccion, ocultamos que estamos evaluando si el auto esta apagado
mi_auto.conducir()    