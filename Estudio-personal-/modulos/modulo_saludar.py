import modul1  


# el metodo pasa de una funcion a ser un metodo 

#variables modulo , m cadena(funcion) , argumentos 
saludo = modul1.saludar('John')
print (saludo)

# funcion as ,renombrar el modulo 
#hacer referencia algo en vez de variable = "saludar" , saludar as variable 
import modul1 as hello
saludo_2 = hello.saludar("Oscar")
print (saludo_2)

#Desde el modulo importamos dos funciones , en este caso son saludos 
from modul1 import saludar as sal , saludar_raro as raro
saudo3 = raro("pepito")
print(saudo3)

saludo_raro =raro("Osuelito")
print(saludo_raro)

print (dir(hello)) # podemos ver todo lo que podemos hacer, nos muestra propiedades 

print(raro.__name__) #devuelve nombre del modulo orginal 

from funciones.m_saludar_2 import saludar_baron as baron # usamos el punto para entrar al archivo 
saludo4= baron("Aurelio")
print(saludo4)


# Agregar modulos fuera de la misma ruta 

#sys, funcion integrada en python , contiene funciones y variables para acceder a parametros y funciones especificas
import sys 
print(sys.path)
# con path podemos ver las rutas de que tiene 
# con append podemos agregar una nueva ruta a la propiedad path 

#agregamos una ruta de carpeta exterior. 
sys.path.append('C:\\Users\\Camilo Prato\\Documents\\Estudio-personal-\\funciones_buenas')
#aqui no podemos usar from ya que 'funciones_buenas' no es un paquete 
import rarito as raron
print (raron.saludando('Bestia'))
        #nombre archivo . nombre de funcion del archivo 
