

import numpy as np 


#creacion de arrays 

# 1 dimension
arrai = np.array([1,2,4,5,6])
print(arrai)

#  2D array          # fila 1  fila 2 
arrai2d = np.array([[1,2,3,4], [5,6,7,8]])
print(arrai2d)

#3d array 
arrai3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arrai3d)


# arrays funciones especiales 

#array ceros 
zeros = np.zeros((3,4)) # filas , columnas 
print (zeros)

#array de unos 
ones = np.ones((2,3))
print(ones)

# array 2*2 de 7 
full = np.full((2,2), 7) 
print(full)

#matriz de identidad
identy = np.eye(3)
print(identy)

#Rangos 
range_arr = np.arange(0,10,2) # crea una matriz 1d de 0 a 10 saltando de a 2 
print(range_arr)

#arrays aleatorios 
random_arr = np.random.random((2,3)) #primero se llama al submodulo y leugo a una funcion en especifico 
print(random_arr) # imprime arrays randoms decimales
#enteros aleatorios  
random_int = np.random.randint(1, 10, (3, 3)) # 3*3 con numeros aleatorios del 1 al 10 
print(random_int)


#Propiedades de los arrays 
arra = np.array([[2,3,4,5], [2,3,4,5]]) # filas , columnas
arra2 = np.array([2,3,4,5])
arra3 = np.array(['hola payaso']) #tamaño si usas shape 
print(arra2.shape) # forma , tamaño 
print(arra2.ndim) # dimensiones
print(arra.size) # N total de elementos
print(arra3.dtype) # tipo de dato
print(arra.itemsize) # tamaño de bytes de cada elemento 

#Tipos de datos 

arr_int = np.array([1,2,3], dtype=np.int32)
arr_float = np.array([1, 2, 3], dtype=np.float64)
arr_complex = np.array([1+2j, 3+4j], dtype=np.complex128)

arr_c = np.array([1.6 , 2.7 , 3.9])
#convertimos a enteros
arr_int = arr_c.astype(int)
print(arr_int.dtype)
print(arr_int)


#OPERACIONES BASICAS 

a = np.array([1,2,3,4])
b = np.array([1,2,3,4])

# operaciones 
suma = a+b 
resta = a-b 
producto = a*b 
division = a / b 
potencia = a**2 
print('Operaciones')
print(potencia)

#Operaciones Escalares 
escalar = a + 10 
multiplicar = a * 10 
print(multiplicar)

#FUNCIONES MATEMATICAS 

arr = np.array([1,23,3,5,6])
raiz = np.sqrt(arr)
loga = np.log(arr)
seno = np.sin(arr)
coseno = np.cos(arr)
exponencial = np.exp(arr)
print(coseno)

#funciones de redondeo 
arr2  = np.array([1.2,23.5,3.6,5.8,6.1])
decimales = np.round(arr2) # redondea
techo = np.ceil(arr2)# aproxima siempre
piso = np.floor(arr2) # nos da el numero sin aproximar
print(piso)