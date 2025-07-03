

class Persona: 
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad 
    
    @property # decorador especial para las clases , ayuda pra entender que lo que tenemos abajo es un get, y asi popdemos eliminar el parentesis 
    #def get_nombre(self), tambien lo podemos hacer de esta manera cuando no usamos la propiedad de "property"
    def nombre(self): 
        return self._nombre
    
    @nombre.setter # podemos establecer o cambiar el valor de nombre 
    def nombre(self, new_nombre): 
        self._nombre = new_nombre
    
    @nombre.deleter
    def nombre(self): 
        del self._nombre 

persona_1 = Persona("camilo", 12)

#Estamos cambiando el valor graicas a la propiedad .setter
persona_1.nombre = "lucas"

# con esto podemos eliminar nombre , gracias a la propiedad deleter
#del persona_1.nombre

# gracias a property podemos llamar a nombre como propiedad y no como funcion 
camilo = persona_1.nombre 



print(camilo)