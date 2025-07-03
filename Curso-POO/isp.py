

from abc import ABC, abstractmethod

class Trabajador(ABC):

    @abstractmethod
    def trabajar():
        pass


class Comedor(ABC):

    @abstractmethod
    def comer():
        pass


class Durmiente(ABC):

    @abstractmethod
    def dormir():
        pass

class Humano(Trabajador, Durmiente, Comedor):
     
    def comer(self):
        print("el humano esta comiendo")
    def dormir(self):
        print("el humano esta durmiendo")
    def trabajar(self):
        print("el humano esta trabajando")

class Robot(Trabajador):

    def trabajar(self):
        print("el robot esta trabajando")

robot1 = Robot()
robot1.trabajar()
