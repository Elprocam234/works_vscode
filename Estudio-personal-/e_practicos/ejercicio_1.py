cursos = {
    "c_actual" : 1.5,
    "c_ minimo" : 2.5,
    "c_prom" : 4,
    "c_max" : 7
}
#hacer promedio de datos
prom_datos = sum(cursos.values()) / len(cursos)
#print(prom_datos)

# hacer suma en un diccionario 
suma_total = sum(cursos.values())
porcentajes = {clave: (valor / suma_total) * 100 for clave, valor in cursos.items()}
print (porcentajes)

#hallar el porcentaje del amyor al actual 

c_actual = 1.5
c_minimo = 2.5
c_prom = 4
c_max = 7 


#crudos 
crudo_promedio = 5 
crudo_video = 3.5 


print("--------------------")

#difrencia del curso actual con el mas rapido de todos 
diferencia_porcentaje = abs(c_actual - c_minimo) / c_minimo * 100
print(f"La diferencia del cursos actual con el mas rapido es de : {diferencia_porcentaje}%")

#diferencia con el curso actual con el mas lento de todos
diferencia_porcentaje2 = (100 - int(abs((c_actual / c_max * 100))))
print(f"La diferencia del curso actual con el mas lento de todos es de : {diferencia_porcentaje2}%" ) 

#diferencia del cursos actual con el promedio 
diferencia_porcentaje3 = 100 - (abs(c_actual / c_prom) *100)
print(f"La diferencia entre el curso actual y el promedio es de : {diferencia_porcentaje3}%")

print("--------------------")
#mostrando el porcentaje que se quita usando los crudos 

porcentaje_promedio_crudo = 100 - (abs(c_prom / crudo_promedio) * 100)
print(f"El porcentaje que se quita del video es de: {porcentaje_promedio_crudo}%")

porcentaje_promedio_crudo = 100 - (abs(c_actual / crudo_video) * 100)
print(f"El porcentaje que se quita del video es de: {porcentaje_promedio_crudo}%")

print("--------------------")
# relacion entre los otros cursos prom y el cursos actual
print(f"ver 10 horas de este curso equivale a ver:  {(abs(c_prom / c_actual)*10):.2f} horas de los otros cursos")
print(f"ver 10 horas de los otros cursos equivale a ver:  {(abs(c_actual / c_prom)*10):.2f} horas de este curso")