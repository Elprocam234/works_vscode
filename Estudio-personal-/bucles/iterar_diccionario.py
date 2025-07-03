diccionario = {
    "nombre" : "camilo",
    "apellido" : "prato"
}

#iterar el conjunto devuelve una tupla
for key in diccionario.items():
    print(key)

for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es : {key} y el valor es: {value}")    