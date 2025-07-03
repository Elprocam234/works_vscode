
def resta():
    entrada = int(input("Escriba la cantidad de numeros que desee restar: "))
    valores = []
    for n in range(entrada):

        n_base = int(input("Escribe el numero base: "))
        n_resta = int(input("Escriba la cantidad de numeros que resten el numero base: "))
        resta = n_base
        n_totales= 0

        for i in range(0, n_resta):
            numeros = int(input(f"Escriba {i + 1} numero/s que resten a {resta}:  "))
            n_totales += numeros
            resta -= numeros    

        texto = (f"La operacion de {n_base} al restar {n_totales} da como resultado: {resta} ")
        valores.append(texto)

    return valores
    
restita= resta()
print(restita)

