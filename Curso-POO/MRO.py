
#MRO es el orden de resolucion del metodo 

class a: 
    def hablar(self): 
        print("Hola desde A")
       

class f(a): 
    def hablar(self):
        print("te hablo desde f")

class b(a): 
    pass
    
class c(f): 
    pass
        
class d(b,c):
    pass

# tomara el primer metodo b , como este metodo tiene es una subclase entonces luego ira para a , en caso que no encuentre ningun metodo 
#ira para c y luego para "a" y  "c" no tiene ningun metodo 


imprime = d()
imprime.hablar()

#imprimos el orden de la clase y los llamados de cada una 
print(d.mro())


#  Imprimos el metodo usando tomando como referencia un objeto ya que creado, en este caso "d" sera self
f.hablar(d)

