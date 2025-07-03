dict = {
    "nombre" : "camilo prato",
    "edad" : 21,
    "subs" : 44444
    #is divided is two : keys , data :  the data, which isnt number, doesnt need quotation marks  .
}

claves = dict.keys() # returns the keys 
print(claves)

claves = dict.get("nombre") #returns the data 
print(claves)

#eliminate the data from the dictionary 
#dict.clear()

dict.pop("nombre") # hacemos una execpion para que no muestre la clave ni el dato de nombre 
print(dict)

item_dic = dict.items()
print (item_dic)