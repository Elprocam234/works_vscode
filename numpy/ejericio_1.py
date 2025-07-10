


import numpy as np 

# 1. Crear un array 1D con números del 1 al 20
# 2. Convertirlo a un array 2D de forma 4x5
# 3. Encontrar la suma de cada fila
# 4. Encontrar el elemento máximo y su posición
# 5. Crear una máscara booleana para elementos mayores a 10

#rango
arr  = np.array(range(1,21))
print(arr)
#shape 2d
arr_2d = arr.reshape(4,5)
print(arr_2d)
#hallar la suma por filas 
sum = np.sum(arr_2d, axis=1)
print(sum)
#encontrar elemento maximo 
max = np.max(arr_2d)
print(max)
#encontrar la posicion de ese elemento 
position = np.argmax(arr_2d)
print(position)




