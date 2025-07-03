

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
        #super() Pertimite heredad atributos y metodos de la clase padre 
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo 
        self.sueldo = sueldo 
    
class Artista: 
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"         
        #cuando queremos llamar esta funcion en otra, usamos return para guardar el valor y poder llamarlo en otra clase 
    
class EmpleadoArtista(Empleado,Artista):
    def __init__(self, nombre, edad, nacionalidad, trabajo, sueldo,habilidad,empresa):
        Empleado.__init__(self,nombre,edad,nacionalidad,trabajo, sueldo)
        Artista.__init__(self,habilidad)
        self.empresa = empresa 

    def presentarse(self):
        #super accede a la clase padre
        return super().mostrar_habilidad()
    
    def mostrando_habilidad(self):
        print(f" Hola soy {self.nombre} y mi habilidad es: {self.mostrar_habilidad()}") 
        return

    def __str__(self):
        return f""" 
        Nombre : {self.nombre}
        Edad : {self.edad}
        nacionalidad : {self.nacionalidad}
        trabajo : {self.trabajo}
        Sueldo : {self.sueldo}s
        Empresa : {self.empresa}
        Habilidad : {self.habilidad}

    """
        
pedro = Empleado("Camilo", 12, "veneco", "agropecuario", 12000 )

print(pedro.nacionalidad)
print(pedro.sueldo)

#imprimios el metodo hablar 
pedro.hablar()

#añadimos datos para luego imprimir como un metodo str 
Santiago= EmpleadoArtista("Santiago", 12,"veneco","agrupecuario",12000,"Cantar","apple")
print(Santiago)

#Santiago.mostrando_habilidad()     
camilo = Artista("Dormir")

#imprimmos la hablidad ya que la funcion no cuenta con un print para mostrar en pantalla
print(camilo.mostrar_habilidad())

#print
Santiago.mostrando_habilidad()

#verificar clases y subclases 


#verificamos si EmpleadoArtista es una subclase de artistica 
herencia = issubclass(EmpleadoArtista, Artista)
print(herencia)


#verificamos si EmpleadoArtista es una subclase de Empleado 
herencia_2 = issubclass(EmpleadoArtista, Empleado)
print(herencia_2)


#verificar si un objeto es una instancia de una clase , tambien las instancias heredan sus clases padres 
instancia = isinstance(Santiago, EmpleadoArtista)
print(instancia)

