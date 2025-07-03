# las clases mayores no pueden depender de una clase menor 

from abc import ABC, abstractmethod 

class VerificadorOrtografico(ABC): 
    @abstractmethod
    def verificador_palabras(self):
        pass

class Diccionario(VerificadorOrtografico):
    def verificador_palabras(self,palabra):
        pass
    #logica para verificar las palabras si estan en el diccionario

class CorrectorOrtografico(VerificadorOrtografico):
    def __init__(self,verificador):
        self.verificador = verificador
    def corregir_texto(self):
        #usamos el verificador para corregir texto 
        pass

#hacer que las clases dependan de una interfaz no de un metodo en especifico 
# las clases padres no pueden depender de la clase hija, para esto debemos de dividir en interfaces 

    
        