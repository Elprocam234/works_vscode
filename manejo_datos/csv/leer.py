

import csv

with open("Manejo Datos\datos.csv", "r", encoding="utf-8" ) as archivo:

    #csv.reader, combierte el archivo en un objeto de puntos y comas, donde separa las columnas por comas
    lectura = csv.reader(archivo)
    
    #next, avanza el iterador una posicion, lo usamos aca para que nos de los encabezados
    encabezados = next(archivo)
    
    print(f"los encabezados son: {encabezados}")

    for filas in lectura:

        print(filas)
        
        #las fila es una lista y podemos acceder a ellas por su indice 
        nombre= filas[0]
        edad= int(filas[1])
        pais= filas[2]    

#me retorna el ultimo valor del for
print(f"nombre: {nombre} , edad : {edad} , pais: {pais}") 