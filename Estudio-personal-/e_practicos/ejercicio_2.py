

# Ejericcio A 

frase = input("Comentanos la frase que deseas decir para conocer cuanto tiempo tardarias: ")
palabras = frase.split() #divide una cadena de texto en subcadenas 
print (palabras)
cantidad_palabras = int(len(palabras)) # len cuenta caracteres pero cuando usamos split para divir se , cuenta los elementos de la lista
tiempo = cantidad_palabras / 2
t_dalto = tiempo * 0.3
if  (tiempo > 60):
    print("para flaco tampoco te pedi un testamento")
else :
    print (f" La cantidad de tiempo que tardara en decir la frase son de : {int(tiempo)} segundos, y dijo {cantidad_palabras} palabras" )    
    print(f"dalto tardaria {t_dalto} segundos")


