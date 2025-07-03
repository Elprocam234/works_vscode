# posicionar parametros 

def frase(nombre,apellido,adjetivo):
    print(f'hola que tal {nombre} {apellido} eres un {adjetivo}')
frase ('camilo', 'prato', 'capo')

# obligar a cambiar de posicion 
frase (nombre='prato', apellido='camilo', adjetivo='sapos')

#funcion con parametro opcional y uno por defecto 
def nombre (nombre,apellido='tonto'): #parametro opcional
    print(f'hola que tal {nombre} {apellido}')
nombre('camilo', 'cabezon') # parametro por defecto

