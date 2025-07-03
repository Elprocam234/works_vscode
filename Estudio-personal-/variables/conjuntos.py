#creando conjunto con set 
conjunto = set (["hola", "ojuela"]) # nos permite crear un conjunto que no se puede modificar 
# el set se crea como lista por dentro, ya que solo permite un argumento
# nos ayuda a almacenar valores unicos y realizar operaciones matematicas. 
print (conjunto)

#anidando conjuntos
conjunto1 = frozenset(["hola muñeco", "como estas"])
print ( conjunto1)
# en el conjunto dos estamos empaquetando el conjunto y una cadena de texto 
conjunto2 = {conjunto1, "hola muñeco"}
print (conjunto2)

# subconjuntos 
c_1 = {1,2,3,4,5}
c_2 = {1,3,5}

#vericar si es un subconjunto 
resultado2 = c_2.issubset(c_1) # issubset, quiere decir que los valores de c1 tambien estan c2, o si es un subconjunto 
print(resultado2)
#verficar si es superconjunto 
resultado = c_1.issuperset(c_2) 
print(resultado)

#verificar si hay un numero en comun 
resultado = c_2.isdisjoint(c_1) # nos da true cuando son diferentes y false cuando son iguales.

print(resultado)