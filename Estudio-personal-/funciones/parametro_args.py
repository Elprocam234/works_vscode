
#forma no optima de sumar numeros 
def suma(lista): 
    n_sumado = 0
    for numero in lista: 
        n_sumado += numero 
    return n_sumado

valor_sumado = suma([1,2,3,4,5])
print(valor_sumado)

# sumar numeros con parametros args
# args se usa para aceptar cualquier cantidad de argumentos 
def saludar(*args):
    for nombre in args: 
        print (f'hola {nombre} como estas')
        
saludar('camilo', 'sofia', 'sharif', 'daniel')

# parametro args para sumar numeros 
def suma(*numeros): # siempre args es el ultimo argumento 
    return print(f'la suma de tus numeros es : {sum(numeros)}')
suma (1,10,10,10)

 #funcion args de manera menos limitada
def suma_total(numeros2):
    return print(f'la suma de los numeros es de = {sum([*numeros2])}')
suma_total([2,3,4,5,2])