# plantilla que ayuda a crear nuevas clases 
 
# implementacion : definir como funcionara un metodo 

from abc import ABC , abstractclassmethod

# aqui hemos creado una plantilla , no se podra usar como instancia directamente 
class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre ,edad ,sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad 
    #Este decorador quiere decir que este metodo debe ser implementado en las subclases
    @abstractclassmethod
    def hacer_actividad(self): 
        pass
    
    def presentarse(self): 
        print(f"hola como estas soy {self.nombre} y tengo {self.edad} años")

#ahora vamos a crear clases que podran heredar Persona()
class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self): 
        print(f"Estoy haciendo: {self.actividad}")
        

class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self): 
        print(f"Actualmente estoy trabajando: {self.actividad}")
        


camilo = Estudiante("camilo",12,"masculino", "jugar deporte")
camilo.presentarse()
camilo.hacer_actividad()
pepito = Trabajador("Pepito ", 12, "Masculino", "Con los bolos")
pepito.presentarse()
pepito.hacer_actividad()


