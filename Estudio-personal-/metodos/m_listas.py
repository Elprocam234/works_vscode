lista = list(["hola mundo",23, 23 ,23 , True])
# contando los elementos de la lista 
print (len(lista))
# mirando el  tipo de dato 
print(type(lista))

print(lista)

#agregar un elemento a lista
lista.append("jajajj")
print (lista)

#agregando un elemto en especifico 

lista.insert(2,"hola madre")
print (lista)

# agregando varios a elemntos a una lista 

lista.extend(["hola mama", 2023, True])
print(lista)

#eliminando un elemento de la lista por su indice
print(len(lista))

lista.pop(0) # -1 para eliminar el ultimo elemento, como no hay -1 empezara desde el ultimo y asi sucesivamente.
print(lista)

#removiendo elemento de la lista
lista.remove("hola madre")
print(lista)


# ordenar los elementos de  forma ascendente 
lista2 = list([19,18,17,24,12,54])
lista2.sort()
print(lista2)

#invertir los elementos de una lista

lista2.reverse ()
print(lista2)
# 
lista3 = ([1,2,3,4,5,4,3,2,])
print (lista3)
conjunto = set(lista3) # la funcion "set" sirve para eliminar los datos repetidos 
print (conjunto)

c_encontrado = (["hola mama", 32,23,23]).index(32)
print(c_encontrado)