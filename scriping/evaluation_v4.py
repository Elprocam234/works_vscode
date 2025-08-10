import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from unidecode import unidecode

# =========================
# FUNCIONES DE APOYO
# =========================

def normalize_text(text):
    return unidecode(str(text).lower().strip())

# =========================
# CARGA Y LIMPIEZA DE DATOS
# =========================

data = pd.read_csv('house_fincaraiz.csv')

# Limpieza de columnas numéricas
for col in ['bedrooms', 'bathrooms', 'area_m2']:
    data[col] = data[col].astype(str).str.extract(r'(\d+\.?\d*)').astype(float)

# Limpieza del precio
data['price'] = data['price'].astype(str)
data['price'] = data['price'].str.replace(r'[^\d]', '', regex=True)
data['price'] = pd.to_numeric(data['price'], errors='coerce')
data = data[(data['price'] >= 10_000_000) & (data['price'] <= 3_000_000_000)]
data['price'] = data['price'] / 1_000_000  # Convertir a millones

# Normalizar ubicación para búsqueda posterior
data['location_normalized'] = data['location'].apply(normalize_text)

# =========================
# PREPROCESAMIENTO
# =========================

numeric_features = ['bedrooms', 'bathrooms', 'area_m2', 'latitude', 'longitude']
categorical_features = ['condition', 'location']

preprocess = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), categorical_features)
    ]
)

# =========================
# DIVISIÓN DE DATOS Y MODELO
# =========================

features = ['bedrooms','bathrooms','area_m2','condition','location','latitude','longitude']
target = ['price']

X = data[features]
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Pipeline(steps=[
    ('preprocessor', preprocess),
    ('regressor', LinearRegression())
])

model.fit(X_train, y_train)

# =========================
# EVALUACIÓN DEL MODELO
# =========================

y_pred = model.predict(X_test)
print('📊 Error cuadrático medio:', mean_squared_error(y_test, y_pred))
print('📈 R² score:', r2_score(y_test, y_pred))

# =========================
# ENTRADA DEL USUARIO
# =========================

user_input = normalize_text(input("📍 Escribe el nombre del barrio o zona: "))
matches = data[data['location_normalized'].str.contains(user_input, na=False)]

if matches.empty:
    print(f"❌ No se encontraron ubicaciones relacionadas con '{user_input}'")
    location_final = user_input
    lat, lon = 0, 0
else:
    location_final = matches['location'].mode()[0]
    lat = matches['latitude'].mean()
    lon = matches['longitude'].mean()
    print(f"✅ Ubicación encontrada: {location_final}")
    print(f"🌎 Coordenadas promedio: Latitud: {lat:.4f}, Longitud: {lon:.4f}")

# =========================
# DATOS DE LA NUEVA CASA
# =========================

new_house = pd.DataFrame({
    'bedrooms' : [int(input('🛏️ Número de habitaciones: '))],
    'bathrooms' : [int(input('🚿 Número de baños: '))],
    'area_m2' : [int(input('📐 Área (m²): '))],
    'condition' : [normalize_text(input('🏚️ Condición de la casa (ej: buena, nueva): '))],
    'location' : [location_final],
    'latitude' : [lat],
    'longitude' : [lon]
})

# =========================
# PREDICCIÓN
# =========================

predicted_price = max(model.predict(new_house)[0][0], 0)
print(f"\n💰 Precio estimado: ${predicted_price:,.3f} millones")

if lat == 0 or lon == 0:
    print("⚠️ Advertencia: Coordenadas no encontradas, la predicción puede no ser precisa.")
