frutas = ["banana", "manzana", "pera", "sandia", "guayaba"]
#evitando que se coma la banana con continue 
for fruta in frutas:
    if fruta == "banana":
        continue # en caso que se cumpla la condicion se salta 
    print (f"me voy a comer {fruta}")
#parando en bluce con break 
for fruta in frutas:
    if fruta == "guayaba":
        break
    print (f"me voy a comer {fruta}")
    
# recorrrer una cadena de texto 
cadena = ("hola mama")
for letra in cadena:
    print(letra)

 
# maneras de multiplicar en iteracion , no es la mejor manera de hacerlo 
numeros = [ 1,2,3,4]
n_duplicado = list()
for number in numeros: 
    n_duplicado.append(number * 2)
    print(n_duplicado)

#manera de multiplicar una interacion 
numeros_duplicado = [x * 2 for x in numeros]
print (numeros_duplicado)

