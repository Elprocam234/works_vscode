class Animal:
    def sonido(self):
       return "sonido generico"

class Pato(Animal):
    def sonido(self):
        return "Cuak CUak"

class Tren:
    def sonido(self):
        return "Chu Chu"


animal = Animal()
tren =  Tren()
pato = Pato()

print(tren.sonido())
print(pato.sonido())
print(animal.sonido())

# duck typing, el tipo de clase de un objeto no importa
#si camina como pato, nada como pato,y hace sonido como pato, es un pato 