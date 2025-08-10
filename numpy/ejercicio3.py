# Sistema de ecuaciones:
# 2x + 3y + z = 1
# x + 2y + 3z = 2
# 3x + y + 2z = 3
# 
# 1. Representar como matriz A y vector b
# 2. Resolver usando np.linalg.solve
# 3. Verificar la solución
# 4. Calcular determinante de A
# 5. Encontrar eigenvalores y eigenvectores


import numpy as np
# matriz coeficientes 
a = np.array([[2,3,1], [1,2,3], [3,1,2]])
vecb = np.array([1,2,3])

#linalg.solve toma como primer argumento la matriz y luego el vector , resulve el sistema de ecuaciones lineales Ax=b
x = np.linalg.solve(a, vecb)

#Verify the solution : Calculate A @ x 
# Using the operator for matrix multiplication 
Ax_calculated = a @ x

#Print array 
print(a)

# Print verify solution 
print(Ax_calculated)

are_they_close = np.allclose(Ax_calculated, vecb)

# if true so its okey 
print(are_they_close)