

#Enviamos un mensaje que actura diferente dependiendo del obejto 
class Perro: 
    def sonido(self):
        return "Guau" 

class Gato: 
    def sonido(self):
        return "Miau"
# 1 tipo de polimorfismo   
animal1 = Perro()
animal2 = Gato()

# estamos utilizando el mismo mensaje pero diferente clase 
print(animal1.sonido())
print(animal2.sonido())

#2 tipo de polimorfismo 
def hacer_sonido(animal):
    print(animal.sonido())
        #animal es el parametro , el sonido() es el metodo 

hacer_sonido(animal1)

#duck typing 
# si un objeto tiene el metodo necesario , funciona sin importar la clase


# enlaces dinamicos y estaticos
# Enlace estatico - la llamada y la ejecucion se resuleve antes de correr el programa, ideal cuando no hay polimorfismo
# por ejemplo una funcion de suma, no importa el tipo de la variable siempre sera una suma 
# Enlace dinamico - Mayor flexibilidad , la desicion la hace en la ejecucion del codigo , si hay polimorfimo


# tipo real y tipo declarado 
#Tipo real - es el tipo de dato que una variable contiene en ese instante 
#tipo declarado - Es lo que esperamos o sugerimos que la variable sea 



