
class Persona:
    def __init__(self, nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad.lower()

    def hablar(self): 
        if self.nacionalidad == "colombiano":
            print(f"Chamo tu eres colombiano")
        else: 
            print(f"Chamo tu no eres colombiano, si acaso veneco")

#tomamos la herencia de Persona , ya que el empleado tambien es persona 
# las herencias tambien heredan metodos 
class Empleado(Persona):

    def __init__(self, nombre, edad , nacionalidad,trabajo, sueldo):
        #Aqui estamos diciendo que quiero que herede de la clase anterior 
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo 
        self.sueldo = sueldo 
    
        

pedro = Empleado("Camilo", 12, "veneco", "agropecuario", 12000 )
print(pedro.nacionalidad)
print(pedro.sueldo)
pedro.hablar()


        