# usamos lambda para crear funciones anonimas, no tienen un nombre 
# lo usamos cuando son funciones pequeñas 

# sintaxis = lambda argumentos = expresion 

# ejemplo donde asignamos a sumar, no le dimos un nombre solo se lo asignamos a sumar 
sumar = lambda a,b : a + b 
print(sumar(4,3))

#lambda es usada en funciones de orden superior 

# map una funcion de orden superior, toma una funcion y un iterable, y aplica esta funcion a cada elemento del iterable 
numeros = [1,2,3,4,54]
# le colocamos una ',' para colocar el objeto iterable 
potencia = map(lambda x : x ** 2, numeros)  
# lo convertimos en una lista ya que lo estamos iterando
print (f'el ejemplo para map es :{list(potencia)}')

# filter, filtra los elementos de una secuencia ite rable 
numero = (1,2,3,4,5)
pares = filter(lambda x : x % 2 == 0, numero)
print(f'el ejemplo para filter es :{list(pares)}')

# sorted (), ordena los elementos de un iterable y devuelve una lista ordenada 
# sintaxis = sorted(iterable, key=None, 
# su orden es diferente ya que la funcion de sorted es ordenar el iterable
tupla = [(1, 'uno'), (2, 'dos'), (3, 'tres')]
ordenado = sorted(tupla, key = lambda x : x[0]) # ordenamos teniendo en cuenta la posicion inicial de la lista
print(ordenado) 
