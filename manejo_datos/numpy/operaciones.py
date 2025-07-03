#operaciones aritmeticas 

import numpy as np 

array = np.arange(0,10)

data = 1 
suma = data + 100
producto = data * 2 
print(f"suma vectorizada  {suma}")

#operaciones universales 
print (f"raiz cuadrada de suma {np.sqrt(array)}")
print(f"\n")
print (f"seno de suma {np.sin(array)}")

# broadcasting : Numpy puede operar con arrayz de diferentes formas 
matriz = np.ones((3,3)) #matriz llena de unos de 3*3
vector = np.arange(3) # o , 1 , 2 
suma_broadcast  = matriz , vector
print( f"suma de matriz y vector {suma_broadcast}")

