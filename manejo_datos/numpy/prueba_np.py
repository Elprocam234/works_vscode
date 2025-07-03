

import numpy as np 
#numpy nos proporciona un objeto multidimensional y herramientas para el funcionamiento del mismo 
# sirve para el manejo de arrays, operaciones matematicas, funciones 


#Maneras de crear arrays 

#listas 
lista = [1,2,3,4,5]
mi_array = np.array(lista)
print(mi_array)

#funciones mumpy
#np.arange(inicio, fin, paso)
array_rango = np.arange(1,10,2)
print(array_rango)

#np.zeros(shape) , crea un array de ceros "shape" es una tupla que define las dimensiones
array_ceros = np.zeros((2,3)) # 2filas y 3columnas
print(array_ceros)

#np.ones(shape) crea un array de unos, funciona igual que el zeros 
array_one = np.ones((2,3))
print(array_one)

#np.linspace (inicio, fin, num_puntos) crea un arrray con puntos espaciados uniformemente 

array_pace = np.linspace(1,10,10) 
print(array_pace)


#conocer dimensiones de mis arrays 
print(f"Estas son las dimensiones del array de zeros: {array_ceros.ndim}")
print(f"Estas son las dimensiones del array de linspace: {array_pace.ndim}")


#Shape es una tupla con el tamañor del array 
print(f"Este es el tamaño del array de ceros: {array_ceros.shape}") #cuando hay 2 dimensiones devulve tupla con filas y columnas 
print(f"Este es el tamaño del array de ceros: {array_pace.shape}") # cuando hay 1 dimension devulve tupla con numero de elementos

#dtpye devulve el tipo de datos de los elementos 
print(f"Este es el tipo de elemento del array de ceros : {array_ceros.dtype}")