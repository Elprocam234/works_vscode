
while True: 
    print ('Bienvenido a la calculadora matematicas')
    print ('1.Suma')
    print ('2.Resta')
    print ('3.Multiplicacion')
    print ('4.Potencia')
    print ('5.Raiz')
    
    option= input ('Elije un numero del (1-5): ')

    if option == '1' : 
        #importar modulo suma
        from suma import suma 
        print (suma)
    
    if option == '2' : 
        #importar modulo suma
        from resta import resta 
        print (resta)
    if option == '3' : 
        #importar modulo suma
        from multiplicacion import multiplicacion 
        print (multiplicacion)
    if option == '4' : 
        #importar modulo suma
        from potencia import potencia 
        print (potencia)
    if option == '5' : 
        #importar modulo suma
        from raiz import raiz 
        print (raiz)
    break