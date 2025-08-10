from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
    
import pandas as pd 
from datetime import datetime
for n in range(2,30):
    driver = webdriver.Chrome()
    driver.get(f'https://www.fincaraiz.com.co/venta/casas/cucuta/norte-de-santander/pagina{n}')

    wait = WebDriverWait(driver, 10)

    #Esperar que cargue el listado 

    #Extraer los datos de las cards 
    cards = driver.find_elements(By.CSS_SELECTOR, 'div.listingCard a.lc-cardCover')
    enlaces = [card.get_attribute('href') for card in cards]



    #lista donde se guardaran los datos 
    datos_propiedades = []


    #Recorrer cada enlace 

    for url in enlaces: 
        # abrimos una pestaña con javascript
        driver.execute_script(f"window.open('{url}', '_blank');")
        
        #esperar que se abra la pestaña 
        wait.until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        
        try: 
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.property-typology-tag-desktop span')))
            #Extraemos todos los datos del span
            spans = driver.find_elements(By.CSS_SELECTOR, 'div.property-typology-tag-desktop span')
            precio = driver.find_element(By.CSS_SELECTOR, 'span.price strong')
            ubicacion = driver.find_elements(By.CSS_SELECTOR, 'div.ant-col p')
            estado = driver.find_element(By.CSS_SELECTOR, 'span.property-tag')
            
            script_tag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//script[@type='application/ld+json']")))
            
            #extraemos el contenido 
            json_text = script_tag.get_attribute('textContent')
            if json_text and json_text.strip():
                data = json.loads(json_text)
                if 'object' in data and 'geo' in data['object']: 
                    latitude = data['object']['geo']['latitude']
                    longitude = data['object']['geo']['longitude']     
           
            #obtenemos los datos en una lista texto 
            texto = [ ]
            for span in spans: 
                texto.append(span.text)

            #generamos una lista nueva 
            lista_nueva = [elemento for elemento in texto if elemento.strip() != '']
            
            #Asignamos valores segun sea el orden 
            habitaciones = lista_nueva[0]
            baños = lista_nueva[1]
            area = lista_nueva[2]
            
            text = []
            
            for map in ubicacion: 
                text.append(map.text)
            
            list_nueva = [ubi for ubi in text if ubi.strip() != '']
            
            ubicacion_actual = list_nueva[1]
    
            
            #asignamos un id para las propiedades 
            id_propiedad = f'P{int(time.time())}_{enlaces.index(url)}'
            
            #guardamos informacion en un diccionario
            propiedad = {
                'id' : id_propiedad,
                'url' : url,
                'habitaciones' : habitaciones,
                'baños' : baños,
                'area' : area,
                'precio' : precio.text,
                'scraped_at' : datetime.now(),
                'Estado' : estado.text,
                'ubcacion' : ubicacion_actual,
                'latitud' : latitude,
                'longitud' : longitude
               
                
            }
            
            datos_propiedades.append(propiedad)
            
            print(f'Habitaciones: {habitaciones}, Baños: {baños}, Area: {area} Precio: {precio.text} Estado: {estado.text} Longitud: {longitude} Latidud: {latitude}')
        except Exception as e : 
            print(f'el error fue : {e}')
        
        driver.close()
        driver.switch_to.window(driver.window_handles[0])


    df = pd.DataFrame(datos_propiedades)
    #mode a , dice que si ya existe el archivo, solo adjunta las nuevas filas , head significa que no incluira el encabezado 
    df.to_csv('house_fincaraiz.csv', mode= 'a', header=False, index=False)
    print('Los datos han sido guardados ')
    print(n)
