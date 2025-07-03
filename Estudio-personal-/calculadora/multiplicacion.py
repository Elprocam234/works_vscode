def multiplicacion(): 
    entrada = int(input('Escribe la cantidad de numeros a multiplicar: '))
    total = 1
    for n in range(entrada): 
        numeros = int(input(f'Escriba el {n+1} numero:'))
        total *= numeros
    return total
total = multiplicacion()
print(total) 
