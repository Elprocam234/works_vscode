def raiz ():
    entrada = int(input('Escriba el numero de raices que desea hallar: '))
    raices = []
    for n in range(entrada): 
        radicando = int(input(f'Escriba el radicando de la {n + 1}  raiz : '))
        indice = int(input(f'Escriba el indice de la {n + 1} raiz : '))
        radical = 1 / indice
        if radicando < 0 and indice %2 != 0:
            resultado = -(pow((-radicando),radical))
        elif radicando < 0 and indice %2 == 0: 
            print('Esta raiz par no tiene numero')
            resultado = None
        else:
            resultado = (pow((radicando),radical))
        raices.append(resultado)
    return raices
raices = raiz()
print (raices)