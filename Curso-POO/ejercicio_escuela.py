

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Estudiante (Persona):
    def __init__(self, nombre, edad,grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def grado_estudiante(self): 
        print(f"El grado de {self.nombre} es: {self.grado}")


estudiante1 = Estudiante("camilo", 12, "once")
estudiante1.grado_estudiante()