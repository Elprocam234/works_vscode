#creando una funcion simple 
def bienvenida():
    print ("hola lucas")    
bienvenida()

# funcion que tenga parametros
# los parametros sirve para guardar informacion en la funcion que luego utilizara en la cabecera 
def  saludar(nombre,sexo):  #dentro del parentsis va el parametro 
    sexo.lower() # convierte todo a minuscula
    if (sexo== "mujer"):
        print (f"hola que tal como estas mi maestra {nombre}, como andas")
    else:
        print(f"hola que tal como estas mi maestro {nombre}, como andas")
saludar("dalto", "mujer") #argumentos, valores concretos que aparecen al llamar la funcion 
    
def saludar_s(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"     
    else:
        adjetivo = "mano no se queres" 
        
    print(f"hola {nombre} que tal mi {adjetivo} ")  
    
saludar_s("camilo", "Hombre")

#funcion que nos retoner multiple valores
def contraseña_aleatoria():
    num = input("Escribe un numero para tener tu nueva clave: ")
    chars = "abcdefghijklmñopqrs"
    numero_entero = str(num)
    num = int(numero_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 1
    #print(f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}") Esto sirve para mostrarla 
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    #ahora si quiero que no la muestre debo de hacer 
    return (contraseña,num) # el return detiene la funcion y devuelve un valor en ese momento que luego podemos llamar 

# //  Aqui estamos guardando la clave en password, que es lo que nos retorna y luego la estamos impriendo segun el parametro que nos dan 
#password = contraseña_aleatoria(1)
#print(f"tu nueva contraseña es: {password}")

# // aqui estamos dando un valor a contri para luego imprimirlo 
contri = contraseña_aleatoria()
print(f"tu nueva clave es {contri}")


password,primer_numero = contraseña_aleatoria()
print(f"tu clave es : {password} y el numero usado es {primer_numero}")
