

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
random_arr = np.random.random((2,3)) #primero se llama al submodulo y luego a una funcion en especifico 
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


#INDEXACION O SLICING 

arr = np.array([1,23,3,5,6])
print(arr[0]) # 1 posicion 
print(arr[-1]) # ulima posicion 
print(arr[2]) # 3 posicion 

# modificacion 

arr[0] = 100
print(arr)

#slicing 
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr[2:7])# imprimir la posicion 2 hasta la 7 sin contar la ultima 
print(arr[:5]) #todos los valores hasta la 5 posicion 
print(arr[3:]) #desde la tercera posicion en adelante
print(arr[::2]) # todos los numeros pero de a dos elementos 
print(arr[::-1]) # recorrer al reverso 
# inicio : fin : paso 


#ARRAYS MULTIDIMENSIONALES 
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#acceso por indice
print(arr2d[1,2]) # fila 1 columna 2 
print(arr2d[0]) # fila 1 
print(arr2d[:,1]) # dame todos los elementos de la segunda columna

#slicing avanzado 

print(arr2d[0:2, 1:3])  # [[2, 3], [5, 6]] tomara las filas de 0 a 2 sin incluir 2 y columnas del 1 al 3 sin incluir el indice 3 
            #filas #columnas 
print(arr2d[:2, :2])    # [[1, 2], [4, 5]] 


#Indexacion booleana 

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#crera una mascara booleana 
mask = arr > 3 
print(mask)

#Indices Especificos 
indices = [0,2,4]
print(arr[indices])

#arrays 2d 
arr2d = np.array([[1, 2], [3, 4], [5, 6]])
print(arr2d[[0,0], [1,0]])
            #fila 0 columna 1
            #fila 0 columna 0

# Manipulacion 
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
#reshape pasar a dos dimensiones 
arr_2d = arr.reshape(3,3)  # estamos diciendo que el array lo convierto en 3*3 
print(arr_2d)

# flatten - convertir 1d
arr_1d = arr_2d.flatten() 
print(arr_1d)

#Transposicion 

arr = np.array([[1, 2, 3], [4, 5, 6]])
arr_T = arr.T
print(arr_T) #   # [[1, 4], [2, 5], [3, 6]]
arr_transpose = np.transpose(arr)
print(arr_transpose) #equivalente 

#Union de Arrays 

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Concatenar
concat = np.concatenate([arr1, arr2])  # [1, 2, 3, 4, 5, 6]

# Stack
stack_v = np.vstack([arr1, arr2])  # [[1, 2, 3], [4, 5, 6]]
stack_h = np.hstack([arr1, arr2])  # [1, 2, 3, 4, 5, 6]


#División de Arrays
pythonarr = np.array([1, 2, 3, 4, 5, 6])

arr = np.array([1, 2, 3, 4, 5, 6])

# Split
split_arr = np.split(arr, 3)  # [array([1, 2]), array([3, 4]), array([5, 6])]

# Arrays 2D
arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
vsplit = np.vsplit(arr2d, 2)  # División vertical
hsplit = np.hsplit(arr2d, 2)  # División horizontal
# Split
split_arr = np.split(arr,3)  # [array([1, 2]), array([3, 4]), array([5, 6])]

# Arrays 2D
arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
vsplit = np.vsplit(arr2d, 2)  # División vertical
hsplit = np.hsplit(arr2d, 2)  # División horizontal

# OPERACIONES MATEMATICAS 
# Funciones de agregacion 
arr = np.array([[1,2,3], [2,3,4]])

#Agregaciones basicas 
print(np.sum(arr)) # entrega una suma total del array 
print(np.sum(arr, axis=0)) # suma por columnas 
print(np.sum(arr, axis=1)) #suma por filas 

print(np.mean(arr)) # da un promedio del array 
print(np.std(arr)) #nos devuelve la desviacion estandar 
print(np.var(arr)) # varianza

print(np.min(arr)) # 1 (minimio) dato menor del array 
print(np.max(arr )) # 4 (maximo) dato mayor del array 
print(np.argmin(arr)) # 0 , es el indice del valor mas pequeño 

#OPERACIONES LOGICAS

arr1 = np.array([True, False, True])# dos arrais con valores booleanos 
arr2 = np.array([False, True, True])

print(np.logical_and(arr1,arr2))
print(np.logical_or(arr1,arr2))
print(np.logical_not(arr1))

#comparaciones 
arr= np.array([1,2,3,4])
print(arr > 3 )
print(np.any(arr >3)) #verifica si hay elementos mayores que 3 
print(np.all(arr > 1))  #verica si todos los elementos son mayores a 1 


#FUNCIONES ESTADISTICAS 
arr = np.array([0,1,2,3,4,5,6,7,10,11])
media = np.mean(arr) # hallamos la media 
mediana = np.median(arr)
moda = np.bincount(arr).argmax() # bincout = me hace un contador de las  veces que se repite cada numero , el indice expresa el numero 0= numero 1 
print(moda)

#medidas de dispercion 

varianza = np.var(arr)
desviacion = np.std(arr)
rango = np.ptp(arr)
print(rango)


#correlacion y covariana 
x = np.array([1,2,3,4,5,6])
y = np.array([2,4,6,8,10,12])

#correlacion , la fuerza y direccion de una relacion lineal entre dos variables 
#fuerza , que tan cerca estan los puntos de formar una linea recta 
#direccion , es la variable que tienede a aumentar cuando la otra es positiva o si tiene a disminur cuando la otra aumenta 


correlacion = np.corrcoef(x,y) # calculamos la matriz de correlacion de pearson entre los dos arreglos
print(correlacion[0, 1]) # 1.0 correlacion perfecta 

# Covarianza
covarianza = np.cov(x, y)
print(covarianza[0, 1]) # si imprime 1.0 quiere decir que la coorrelacion es perfecta 
# la covarianza mide como varian dos variables, si es positiva significa que son directas de lo contrario que decir que son inversas 


# OPERACIONES MATRICIALES 

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

#mulptlicacion matricial 
producto = np.dot(0,0) # fila 0 de a y columna 0 de b , los elementos se multplican y se suman 
producto_alt = A @ B   # mismo pero de manera mas clara 
print(producto_alt)

