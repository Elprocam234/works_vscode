

#toma  una funcion como entrada, agrega una mas y luego devuelve otra com entrada , sin cambiar el codigo original de la funcion 

# una funcion decoradora simpere debe recibir como parametro otra funcion 
def decoradora (funcion):
    def funcion_modificada():
        print("Antes de la funcion")
        #aca se imprime la funcion con el parametro que le asignemos , en este caso es saludo 
        funcion()
        print("despues de la funcion")
        #nos retorna la funcion modificada 
    return funcion_modificada


#la funcion saludo es la que vamos a decorar, añadiendo una funcion modificada 
def saludo():
    print("hola como andas")


funcion_modificada2 = decoradora(saludo)
funcion_modificada2()


# a continuacion añadiremos una funcion pero de la manera optima como debe ser 

def decorador(funcion):
    def fun_modificada(): 
        print("Esta es la primera parte que se agrega")
        funcion()
        print("che, esta es la segunda parte que agregamos")
    return fun_modificada

# @decorador es un atajo que lo usamos para decorar funciones, el directamente reemplaza el parametro funcion por la funcion saludar
@decorador
def saludar(): 
    print("vamos que si se puede")
saludar()

# La funcion saludar se convertira en la funcion modificada, de manera interprete ya que no estamos moficando la original , basicamente es coo si hicieramos una copia 
