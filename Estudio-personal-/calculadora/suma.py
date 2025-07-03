
def suma ():
    entradas = int(input('Escribe la cantidad de numeros que deseas sumar: ' ))
    total = 0 
    for n in range(entradas):
        suma = int(input(f'Ingresa el {n + 1 } numero: '))
        total += suma 
    return total
total = suma()

print(total)


    