from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Configurar el navegador 
driver = webdriver.Chrome()
driver.get('https://www.fincaraiz.com.co/venta/casas-y-apartamentos/cucuta/norte-de-santander')

# Esperar que cargue y hacer clic en la primera tarjeta 
wait = WebDriverWait(driver, 10)
enlace = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.listingCard.highlight a.lc-cardCover')))
enlace.click()

#Cambiando a la nueva pestaña 
time.sleep(2) #esperar brevemente para que se abra la pestaña 
driver.switch_to.window(driver.window_handles[1]) # la nueva pestaña es la segunda, indice 1 

#Esperar que cargue el contenido de nuevo,  'presence_of_element_located', verifica la presencia del elemento no su visibilidad
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.property-typology-tag-desktop span.ant-typography-ellipsis-single-line')))

#Extraemos todos los datos del span
spans = driver.find_elements(By.CSS_SELECTOR, 'div.property-typology-tag-desktop span.ant-typography-ellipsis-single-line' )

#Mostrando el contenido 
for span in spans:
    print(span.text)
    
driver.quit()