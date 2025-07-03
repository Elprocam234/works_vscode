

class Miclase:
    def __init__(self):
        #el "_" quiere decir que es privado, nos devolvera el valor pero esto hace entender al programador que es privado
        self._atributoprivado = "valor"

objeto = Miclase()
print(objeto._atributoprivado)

#atributos muy privados   
#los dos guiones bajos no permitira buscarlo 
# class Miclase:
#     def __init__(self):
#         self.__atributoprivado = "valor"

# objeto = Miclase()
# print(objeto.__atributoprivado)

# otra manera usando get y set
 
class Persona: 
    def __init__(self, nombre, edad):
        #el "_" quiere decir que son privados y que tengo que acceder de otra manera
        self.__nombre = nombre
        self.__edad = edad 

        #get y el la variable que desea obtener ,  get significa obtener 
    def get_nombre(self): 
        return self.__nombre

persona_1 = Persona("camilo", 12)

nombre = persona_1.get_nombre()

#son los mismo, diferentes maneras de acceder 
print(persona_1.get_nombre())
print(nombre)

