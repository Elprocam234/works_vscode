def potencia(): 
    entrada = int(input('Escribe la cantidad de numeros para hallar potencia: '))
    resultado = []
    for n in range(entrada): 
        base = int(input(f'Escriba la base del {n+1} numero: '))
        potencia = int(input(f'Escriba la potencia del {n+1} numero: '))
        resultado.append(base ** potencia)  
    return resultado
valor = potencia()
print (valor)

   

 