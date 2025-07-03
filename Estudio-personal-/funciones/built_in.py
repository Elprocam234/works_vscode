numeros = [ 1,2,3,4,5,6]

# econcontrando el numero mas alto y bajo
n_alto = max(numeros)
n_bajo = min(numeros)
print (f"numero alto {n_alto} y numero bajo {n_bajo}")

# redondeando a 6 numero decimales 
numero = round(212.23123,2) #despues de la coma podemos elejir la cantidad de decimales que queremos
print(numero)

# retorna False = 0, false, dato vacio, ninguno o True = un numero distinto a cero 
resultado = bool(0)
resultado = bool(1)
print (resultado)
# retorna True = Si todos los elementos son verdaderos 
n_verdaderos = [1,2,3,4,5]
resultado_all = all(n_verdaderos)
print(resultado_all)

# suma todos los elementos

sum_total = sum(n_verdaderos)
print(sum_total)            

