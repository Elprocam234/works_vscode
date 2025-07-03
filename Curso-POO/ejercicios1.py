class Estudiante: 
    #atributos 
    def __init__(self, nombre, edad, grado,estudiando):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.estudiando = estudiando.lower()

    #metodos

    def estudiar (self):
        if self.estudiando == "si": 
            print(f" {self.nombre} esta estudiando")
        else:
            print(f"{self.nombre} no se puso a estudiar") 
    def __str__(self):
        return (f"""----Datos del Estudiante---- \n
                nombre : {self.nombre}
                edad : {self.edad}
                grado : {self.grado}
                Estudiar : {"El estudiante se puso a estudiar " if self.estudiando == "si" else "No se puso a estudiar"}
                """)

nombre = input("Escribe tu nombre: ")
edad = input("Escribe tu edad: ")
grado = input("Escribe tu grado: ")
estudiando = input("Escribe SI / NO si quieres que estudie: ")

estudiante_1 = Estudiante(nombre,edad,grado,estudiando)
print(estudiante_1)
estudiante_1.estudiar()
