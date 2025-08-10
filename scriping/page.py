from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver # extraemos el modulo webdriver, tiene las funciones necesesarias para interactuar con la pagina 
from selenium.webdriver.chrome.service import Service # importamos service para inciar el servicio de chormedriver
from webdriver_manager.chrome import ChromeDriverManager #importa una clase que se encarga de descargar automaticamente el chormedriver correcto 


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#utlizamos los metodos de extracion que tiene by, css selector, xpath, etc 
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.fincaraiz.com.co/venta/casas-y-apartamentos/cucuta/norte-de-santander"
# Esperamos hasta 15 segundos a que cargue el elemento
try:
    espera = WebDriverWait(driver, 15)
    card = espera.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".listingCard.highlight.CO")))
    card[0].click()
except Exception as e:
    print("No se encontró el elemento:", e)
    driver.save_screenshot("error_captura.png")