


class Persona: 
    def __init__(self, nombre, edad ):
        self.nombre = nombre 
        self.edad = edad 
    # hacemos representacion en un string de los atributos 
    def __str__(self):
        return f"Nombre : {self.nombre}, Edad: {self.edad}"
    
    #hacemos representacion de las atributos y sus argumentos 
    def __repr__(self):
                        #Debemos colocarlo en comillas el nombre ya que nos insteresa que devuelva un str
        return f" Persona('{self.nombre}' , {self.edad})"

    def __add__(self, otro): 
        #verifica si "otro" es una instancia d' persona (si es un objeto)
        if isinstance (otro, Persona):
            #combinamos los nombres 
            nuevo_nombre = self.nombre +  " y  "   + otro.nombre 
            #combinamo slas edades 
            nueva_edad= self.edad + otro.edad
        #retornamos lo nuevos valores 
        return Persona(nuevo_nombre, nueva_edad)

p1 = Persona("samuel",12)      

#obtener una representacion del objeto 
representacion = repr(p1)
#reconstruimos el objeto
resultado = eval(representacion)
print(f"Este fue el resultado al usar la funcion eval: {resultado}")
print(f"Este fue el resultado al usar la funcion repr: {representacion}")


pedrito = Persona("pedrito", 20 )
resultado = p1 + pedrito
print(resultado) 