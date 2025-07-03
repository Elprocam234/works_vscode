#creando dicionarios con dict

diccionario = dict(nombre= "lucas", edad= 19, suscriptores = 2000)

# colocar tuplas en un conjunto
# las listas no pueden ser claves ni elementos ya que no tiene un valor fijo 
dic = {
    ("la mami", "de dalto") : "jjasjjsjsj"
}
print (dic)

#creando diccionarios con fromkeys  

#primera manera
elementos= diccionario.fromkeys(["nombre", "apellido", "edad"]) # lo guardamos dentro de una lista, creamos un diccionario vacios
#segunda manera
diccionario =  dict.fromkeys(["nombre", "varniz"]) # de esta manera creamos diccionarios vacios. 
print (diccionario)
diccionario = dict.fromkeys ("hola") # se pasa una cadena como argumento.
print(diccionario)
diccionario = dict.fromkeys("nombre", "camilo") # nos imprime cadena y valor 
print(diccionario)
diccionario = dict.fromkeys (["nombre, apellido"], "no sé ") #primero lo iterable y luego no iterable 
print (diccionario)
print(elementos)
 
