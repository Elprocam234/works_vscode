

import pandas as pd

from sklearn.model_selection import train_test_split #dividimos los conjuntos en dos partes, entrenamiento y prueba 
from sklearn.linear_model import LinearRegression # Objetivo encontrar la mejor linea recta 
from sklearn.preprocessing import StandardScaler # Estandariza las caracteristicas numericas, desviacion estandar de 0 - 1
from sklearn.metrics import mean_squared_error, r2_score # Error cuadratico medio y coeficiente de determinacion R cuadrado, se calcula la diferencia del promedio predicho y el real 
from sklearn.preprocessing import OneHotEncoder # Convertir variables categoricas a numericas , creando una tabla binaria 
from sklearn.compose import ColumnTransformer # organiza el preprocesamiento entre variables con diferentes features
from sklearn.pipeline import Pipeline # oeganiza la secuencia de pasos 

# Extracted data
data = pd.read_csv('house_fincaraiz.csv')

#Limpieza de datos
for col in ['bedrooms', 'bathrooms', 'area_m2']:
    data[col] = data[col].str.extract('(\d+\.?\d*)').astype(float)
data['price'] = data['price'].str.replace(r'[^\d.]', '', regex=True).str.replace('.', '', regex=False).astype(float) / 1000000

#variables en minuscula 
for val in ['location']:
    data[val] = data[val].str.lower() 
    
#preprocess the data 
# define numerical and categorical colums 
numeric_features = ['bedrooms', 'bathrooms', 'area_m2','latitude','longitude']
categortical_feautres = ['condition', 'location']

#Create a preprocessor with one-hot encoding for categorical variables 
preprocess = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features), #todos los datos se le haran un preprocesamiento(DVS) y luego se devolveran transformados
        ('cat', OneHotEncoder(drop='first' , handle_unknown='ignore'), categortical_feautres) # se crea una columna binaria de 0-1 , drop first, crea N columans dependiendo de N categorias , le pide que elimine la primera columna , # handle_unknown ignora las categorias desconocidas 
    ]
)


#Select features and target 
features = ['bedrooms','bathrooms','area_m2','condition','location','latitude','longitude']
target  = ['price']


# split data
x = data[features]
y = data[target]

x_train , x_test , y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
                                    #dividmos las varibles en dos subconjuntos, entrenamiento y prueba , el parametro test size, dice que el 
                                    # 20% se destinara para prueba , 80% para entrenamiento , asi podremos saber si realmente el modelo aprendio 
                                    #random_state es la semilla que especifica la mezcla entre el entrenamiento y la prueba, ayuda a que los valores sean identicos      

#create and train the model 
model = Pipeline(steps=[ #creacion de la maquina de predicccion, pipeline es una tuberia o secuencia de pasos
    ('preprocessor', preprocess), # contiene un nombre preprocessor y la variable que definimos anteriormente 
    ('regressor', LinearRegression())  # el modelo aprendera de los datos transformados, el estimado final de la tuberia 
       
])
model.fit(x_train, y_train) #llamamos el metodo .fit de nuestro objeto model  , es el corazon de scikit learn  , cuando se llama en una pipeline hace,
                            #fit(ayuda a concoer la ecuacion que mas se adapta a los datos, su funcion principal es que conozca o aprenda )
                            
#evaluate the model 
y_pred = model.predict(x_test)
print('Error cuadratico medio: ', mean_squared_error(y_test, y_pred))
print('R cuadrado score', r2_score(y_test,y_pred))

new_location = input(f'Escribe la ubicacion de la casa: ').lower()

location_coords = data.groupby('location') [['latitude', 'longitude']].mean().to_dict()
lat = location_coords['latitude'].get(new_location)
lon = location_coords['longitude'].get(new_location)

if lat is None and lon is None: 
    print(f'No se encontraron coordenadas para {new_location}')
else: 
    print(f'Las coordenadas promedio encontradas son : Latitud: {lat}, Longitude: {lon}')


new_house = pd.DataFrame({
    'bedrooms' : [int(input('Escribe el numero de habitaciones: '))],
    'bathrooms' : [int(input('Escribe el numero de baños: '))],
    'area_m2' : [int(input('Escribe el area: '))],
    'condition' : [input('Escribe la condicion de la casa: ').lower()],
    'location' : [new_location],
    'latitude': [lat] if lat is not None else [0],  # Asignar coordenadas o 0 si no existen
    'longitude': [lon] if lon is not None else [0]
        
})

predicted_price = max(model.predict(new_house)[0][0],0) # acedemos a la primera fila extraemos  el primer elementos, son unicos pero asi podemos tener un valor plano
print(f"Precio predicho: ${predicted_price:,.3f} millones")# mostrar float con 2 decimales