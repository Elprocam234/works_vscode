#crear una funcion que al enviar un numero nos genere numeros primos hasta llegar a ese numero 


#creando una funcion que nos devuleva si es primo o no 
def primo (num): 
    for i in range(2, num - 1): 
        if num % i == 0 :
            return False
    return True 

resultado = primo(3)
print(resultado)
        
def numeros_primos (num): 
    lista_primos = []
    for i in range (2, num + 1):
        if primo(i) == True:
            lista_primos.append(i)
    return lista_primos
listas_primos = numeros_primos(15)
print( listas_primos)


# i sí está en un for, pero dentro de una comprensión generadora.
#🔹 all() verifica que todas las condiciones sean True. 
# all es una compresion de generador 

#primos_hasta = lambda num : list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)), range(2,num)))
primos_hasta = lambda num : list(filter(lambda x : all(x % i != 0 for i in range(2, (x ** 0.5) + 1)), range(2,num)))
print(primos_hasta(15))
    
    