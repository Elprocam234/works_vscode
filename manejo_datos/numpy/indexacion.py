

import numpy as np 



array_elementos = np.arange(0,10,1)
print(array_elementos)

#primer elemento 
print(array_elementos[0])

#Segundo elemento 
print(array_elementos[-1])

#Slicing
print(array_elementos[0:5]) 

#data_2d, Indexacion y slicing
array2d = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(array2d)

# para acceder usamos [filas y colunas]
print(array2d[0,1])

# obtener una fila completa
print(array2d[0,:]) #significa todos los elementos de esta dimensión 
#[0,:] (0,) quiere decir fila cero todas las columnas, : slice, en donde tomara todos los valores de esa dimension
# las cosas no estan bien del todo 
