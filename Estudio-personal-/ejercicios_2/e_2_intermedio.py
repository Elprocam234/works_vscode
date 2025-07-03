

###asistencia = int(input('Escriba la cantidad de alumnos que asistieron: '))
#edades = []
#for total in range(asistencia):
  #  edad = int(input('Escriba su edad: '))
 #   edades.append(edad)
#usamos en sort(reverse = true o false ) false es preterminado y quiere decir que no reviertas la lista natural
#edades.sort()
#profesor = max(edades)
#asistente = min(edades)
#print(f'La cantidad de alumnos es: {asistencia}, el profesor es: {profesor} y su asistente es: {asistente}')
   

# lo mismo pero ahora vamos  a usar tambien el nombre 

# practica, el profesor no fue a clase y los alumnos se ordenaron : el mayor sera el profe y el menor el asistente

compañeros = []

#cremos la funcion para obtener asistente y profesor 
def estudiantes(cantidad_estudiantes):
  for i in range(cantidad_estudiantes):
    nombre = input('Escriba su nombre: ')
    edad = int(input('Escriba su edad: '))
    #empaquetamos los valores en una variable
    compañero = nombre,edad
    # A los valores de la variable la envaimos a una lista 
    compañeros.append(compañero)
    #con sort organizamos los valores de la lista
  compañeros.sort()   # sort(reverse False o true) False es de menor a mayor y true es al revez
  #hallammos el nombre del compañero segun su posicion, primero entramos a la posicion de la lista y luego a los datos
  profesor = compañeros[-1][0]
  asistente = compañeros[0][0]
  #retornamos los valores para luego igualarlos fuera de la funcion
  return profesor,asistente 

n_profesor, n_asistente =  estudiantes(2)
print(f'el profesor es {n_profesor} y el asistente {n_asistente}')
        
