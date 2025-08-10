from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Configurar el navegador 
driver = webdriver.Chrome()
driver.get('https://www.fincaraiz.com.co/venta/casas/cucuta/norte-de-santander')

# Esperar que cargue y hacer clic en la primera tarjeta 
wait = WebDriverWait(driver, 10)
enlace = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.listingCard.highlight a.lc-cardCover')))
enlace.click()

#Cambiando a la nueva pestaña 
wait.until(EC.number_of_windows_to_be(2))  # Esperar a que se abra la nueva pestaña
driver.switch_to.window(driver.window_handles[1]) # la nueva pestaña es la segunda, indice 1 

#Esperar que cargue el contenido de nuevo,  'presence_of_element_located', verifica la presencia del elemento no su visibilidad en el DOM 
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.property-typology-tag-desktop span')))
#Extraemos todos los datos del span
spans = driver.find_elements(By.CSS_SELECTOR, 'div.property-typology-tag-desktop span')
precio = driver.find_element(By.CSS_SELECTOR, 'span.price strong')

texto = []

#recorremos los spans
for span in spans : 
  texto.append(span.text) 
  
#Generamos una lista eliminando los items vacios 
lista_nueva = [elemento for elemento in texto if elemento.strip() != '']
print(lista_nueva) 

#Asignamos valores segun sea el orden 
habitaciones = lista_nueva[0]
baños = lista_nueva[1]
area = lista_nueva[2]

print(f'Habitaciones: {habitaciones}, Baños: {baños}, Area: {area} Precio: {precio.text}')


# Cerrar el navegador
driver.quit()