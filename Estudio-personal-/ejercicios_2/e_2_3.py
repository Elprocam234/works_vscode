
# definir funcion de fibo 

def fibo(num):
    a,b = 0,1
    lista_fibo = [0] 
    for i in range (num):
        if a + b > num:
            return lista_fibo 
        else:
            lista_fibo.append(b)
            a,b = b, a+b
    return lista_fibo
resultado = fibo(10)
print(resultado)
        
            
        
        
