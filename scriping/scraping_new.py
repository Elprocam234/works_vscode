


import requests as r 
from bs4 import BeautifulSoup as bs


url = 'https://www.fincaraiz.com.co/venta/casas-y-apartamentos/cucuta/norte-de-santander'
asnwer = r.get(url)

soup = bs(asnwer.text, 'html.parser')

properties = []

anuncios = soup.find_all('div', class_='lc-typologyTag')

for item in anuncios: 
    #buscar el span que contiene los datos 
    span_data = item.find('span', class_='body body-2 body-regular medium')
    
    #obtener los strong dentro del span 
    strongs = span_data.find_all('strong')
    
    #extaer los datos segun su posicion
    
    habitaciones = strongs[0].text.strip()
    baños = strongs[1].text.strip()
    metros_2 = strongs[2].text.strip()
    
    print(f'Habitaciones: {habitaciones}, baños: {baños}, metros cuadrados: {metros_2}')
    
# La web scriping 

# Consiste en el uso de programas o scripts que simulan la interacción de un usuario, permite acceder a los datos de una pagina web, buscando información relevante 

# Funcionamiento: 
# Envia una solicitud HTTP a la pagina web puede ser con una librería request 
# Recibe la respuesta normalmente en formato HTML 
# Analizamos el contenido de HTML para localizar los datos de interés, usualmente se usa BeautifulSuop 
# Se extrae los datos deseados y se almacenan en formato csv

# soup = se llama así por convención haciendo referencia a una sopa de etiquetas


# librerías 
# requests = hacer solicitudes HTTP de forma sencilla y eficiente 'HTTP' = Protocolo de transferencia de hipertexto 
# bs4 = Es una biblioteca para analizar documentos HTML y XML y extraer datos en ella 

