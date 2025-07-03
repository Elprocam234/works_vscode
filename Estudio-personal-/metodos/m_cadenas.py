cadena1 = "holA soy dalto"
cadena2 = "1231234"
cadena3 = "gola"

#dir devuelve la lista de atributos validos del objeto pasado
#upper sirve para colocar caracteres en mayuscula 

print(dir("hola mundo"))  #cuando colocamos un objeto al div, nos devulve los metodos y atributos disponibles para ese objeto. 

resultado = cadena1.upper() #todo mayuscula 
resultado2 = cadena1.capitalize() # la primera en mayuscula 
resultado3 = cadena1.lower() # todo minuscula  
resultado4 = cadena1.find("s") #Busca la posicion de una letra en la cadena de texto 
resultado5 = cadena3.isalpha() # NOs devuelve true si tiene caracteres, los caracteres especiales no son alphanumericos
resultado6 = cadena2.isnumeric() # Nos dice si la cadena son numeros
resultado7 = cadena2.count("1") # Nos devuelve el numero de ocurrencias de una subcadena en la cadena dada. 
resultado8 = cadena1.__len__() # Cuenta los caracteres de una cadena. 
resultado8 = len(cadena1) # Cuenta los caracteres de una cadena. 
#para len podemos usarlo de dos formas, por mas de q se una funcion, puede depender del obejto anterior y usamos __len__
empiza_con = cadena1.startswith ("ho")  #vericar con que terminar 
termina_con = cadena1.endswith ("a") #vericar con que  termina 
cadena_nueva = cadena1.replace("holA", "camilo") # reemplaza un valor por otro.
cadena_nueva2 = cadena_nueva.capitalize()
cadena_separada = cadena1.split(" ")
n_caracteres = cadena_separada.__len__() #pasamos de separar a contar los valores de una cadena. 

print (resultado)
print (resultado2)
print (resultado3)
print (resultado4)
print(resultado6)
print (resultado5)
print (resultado7)
print (f"este es: {resultado8}")
print (empiza_con)
print (cadena_nueva)
print (cadena_nueva2)
print (cadena_separada)
print (n_caracteres)