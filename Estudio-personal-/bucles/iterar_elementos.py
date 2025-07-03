# iterando elementos, cadenas de texto
animales = ["gato", "perro", "serpiente", "agua"]
for animal in animales : # se lee como "para cada elemento en el (interable) haz algo"
    print(f"ahora el animal sera {animal}" )

#iterando numeros 
numeros = [ 1,2,3,5]
for numero in numeros :
    resultado = numero * 10 
    print(resultado)

#recorrer dos listas al mismo tiempo con la funcion zip(), las dos listas deben tener la misma cantidad de elemntos. 
# zip () convierte elementos iterables en tuplas
for animal,numero in  zip(animales,numeros): 
    print(f"el animal es : {animal} y el numero atribuido es: {numero}")
    
# hacer un recorrido con range con dos parametros
    for num in range(4,10):
        print (num)
#hacer un recorrido con un parametro
for num in range(20):
    print(num)
    
# forma no optima de recorrer una lista, no sive en conjuntos
number = [1,2,3,4,5]
for numeros in range(len(number)):
    print(number[numeros])

# forma correcta de recorre una lista con su indice
#recorrer una lista con su indice y valor
for numb in enumerate(number):
    print(numb)
#recorre una lista por su indice
for numb in enumerate(number):
    print(numb[0])
#recorre una lista por su valor
for numb in enumerate(number):
    print(numb[1])
#recorre una lista por su indice y valor, enumerate genera tuplas
for numb in enumerate(number):
    print(f"su indice es: {numb[0]} y su valor es:{numb[1]}")
#recorrer la lista con else
for numb in number: 
    print(numb)
else: 
    print("mi hermano ya se acabo la lista")    

#todo tambien sirve para las tuplas y conjuntos
