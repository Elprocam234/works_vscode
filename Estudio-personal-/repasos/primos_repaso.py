# definir si es primo o no 

def prim (num):
    for i in range (2, num-1):
        if num % i == 0: 
            return False
    return True  
resultado = prim(4)
print(resultado)

def numeros_primos(numero): 
    lista_primos = []
    for i in range (2, numero + 1):
        if prim(i) == True:
            lista_primos.append(i)
    return lista_primos
lista_de_primos = numeros_primos(10)
print(lista_de_primos)
        
            
        
    

