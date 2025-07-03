ingreso_mensual = 10000
gasto_mensual = 2000

#Hicimos una prueba con un "if" anidado
if ingreso_mensual > 1000 : 
   if ingreso_mensual - gasto_mensual > 3000 : 
       print ("estas bien")
   else :
       print(" hay revisar como estas")
       
#Hicimos otra prueba con un elif "es como otra opcion en caso que no se de el if"
elif ingreso_mensual >= 10000:
    print ("Eres rico en el mundo")     
    
else : 
    print("estas pobre")    

