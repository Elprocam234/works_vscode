

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
from unidecode import unidecode

#charge the data
data = pd.read_csv('house_fincaraiz.csv')

#funtion normalize text 
def normalize_text(text):
    return unidecode(text.lower().strip()) #pasamos a minusuclas y luego eliminamos acentos

#clean the data
for col in ['bedrooms', 'bathrooms', 'area_m2']:
    data[col] = data[col].astype(str).str.extract(r'(\d+\.?\d*)').astype(float)

#clean the price
data['price'] = data['price'].astype(str)
data['price'] = data['price'].str.replace(r'[^\d]', '', regex=True) 
data['price'] = pd.to_numeric(data['price'], errors='coerce')
data =  data[(data['price'] >= 10_000_000) & (data['price'] <= 3_000_000_000)]
data['price'] = data['price'] / 1_000_000

#normalize the location 
data['normalized_location'] = data['location'].apply(normalize_text)


#Select features and target 
features = ['bedrooms','bathrooms','area_m2','condition','location']
target  = ['price']

#preprocess the data 
# define numerical and categorical colums 
numeric_features = ['bedrooms', 'bathrooms', 'area_m2']
categortical_feautres = ['condition', 'location']


# ======================
# PREPOCESSOR
#======================

#Create a preprocessor with one-hot encoding for categorical variables 
preprocess = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features), #todos los datos se le haran un preprocesamiento(DVS) y luego se devolveran transformados
        ('cat', OneHotEncoder(drop='first' , handle_unknown='ignore'), categortical_feautres) # se crea una columna binaria de 0-1 , drop first, crea N columans dependiendo de N categorias , le pide que elimine la primera columna , # handle_unknown ignora las categorias desconocidas 
    ]
)

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
 
 
# ======================
# Evaluation
#======================
                           
y_pred = model.predict(x_test)
print('Error cuadratico medio: ', mean_squared_error(y_test, y_pred))
print('R cuadrado score', r2_score(y_test,y_pred))


user_input = normalize_text(input(f'Escribe el barrio o zona: '))
matches = data[data['normalized_location'].str.contains(user_input, na=False)]

if matches.empty: # devuelve true si no encuentra coincidencias 
    print('No se encontraron ubicaciones relacionadas con : ', {user_input})
    location_final = user_input
else: 
    location_final = matches['location'].mode()[0]
    print(f'La ubicacion encontrada es: {location_final}')
    
new_house = pd.DataFrame({
    'bedrooms' : [int(input('Escribe el numero de habitaciones: '))],
    'bathrooms' : [int(input('Escribe el numero de baños: '))],
    'area_m2' : [int(input('Escribe el area: '))],
    'condition' : [normalize_text(input('Escribe la condicion de la casa: '))],
    'location' : [location_final]
    
})

predicted_price = model.predict(new_house)[0][0] # acedemos a la primera fila extraemos  el primer elementos, son unicos pero asi podemos tener un valor plano
print(f"Precio predicho: ${predicted_price:,.3f} millones")# mostrar float con 2 decimales