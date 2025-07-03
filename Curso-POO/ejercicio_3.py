


class Personajes:
    #generamos metodo constructor para guardar en memoria
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre 
        self.fuerza = fuerza
        self.velocidad = velocidad 
    #usamos el meotodo repr para representar los valores , nombre de la clase y atributo 
    def __repr__(self):
        return f" Nombre: '{self.nombre}' Fuerza : {self.fuerza} Velocidad: {self.velocidad} "
# Definimos el comportamiento de operadores , ya sea "+*/-", especificamos como debe comportarse en base a las operaciones que le hagamos
    def __add__(self, otro_pj):
        #verificamos que otro sea una instancia de la clase Personajes
        if isinstance (otro_pj, Personajes):
            nuevo_nombre = self.nombre + otro_pj.nombre 
            nueva_fuerza = self.fuerza + otro_pj.fuerza 
            nueva_velocidad = self.velocidad + otro_pj.velocidad 
        return(nuevo_nombre,nueva_velocidad, nueva_fuerza)

#asignamos valores a los personajes 
goku = Personajes("goku", 12, 15)
gohan = Personajes("Gohan", 14, 15)

print(goku)

#Ejecutamos operacion de suma 
fusion = goku + gohan 
print(fusion)


        
        