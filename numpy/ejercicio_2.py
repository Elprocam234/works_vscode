


import numpy as np 
import matplotlib.pyplot as plt 
# 1. Generar 1000 números aleatorios con distribución normal (media=50, std=15)
# 2. Calcular media, mediana, desviación estándar
# 3. Encontrar percentiles 25, 50, 75
# 4. Crear histograma de frecuencias usando np.histogram
# 5. Normalizar los datos (media=0, std=1)


#100 numeros aleatorios, media de 50 , desviacion estandar de 15  y tamaño 1000
arr_random = np.random.normal(loc=50, scale=15 , size=1000)
#print(arr_random)

#calculate the average
arr_average = np.average(arr_random)
print(f'the average is : {arr_average}')
#calculate the median 
arr_median = np.median(arr_random)
print(f'the median is : {arr_median}')
#calculate standard deviation 
arr_std = np.std(arr_random)
print(f'the standard desviation is : {arr_std}')
# calculate percentiles 25 , 50 , 75 
arr_pd1 = np.percentile(arr_random,25)
arr_pd2 = np.percentile(arr_random,50)
arr_pd3 = np.percentile(arr_random,75) 
print(f'The 25th percentile value is : {arr_pd1}')
print(f'The 50th percentile value is : {arr_pd2}')
print(f'The 75th percentile value is : {arr_pd3}')

#Create a histrogram 
arr_htogram = np.histogram(arr_random)

#
plt.hist(arr_random)
#
plt.xlabel('Valor X')
plt.ylabel('Valor Y')
#
plt.title('Histogram the data random')
#
plt.show()


print(arr_htogram)

