


#selenium , conjunto de herramientas librerias que tienen soporte en varios lenguajes 
#Se usa para la automatizacion de interaciones en una pagina web, como clics , formularios o desplazamientos 
# ChormeDriver, es un servidor (puente o traductor) que permite a selenium comunicarse y navegar en chorme



from selenium import webdriver # extraemos el modulo webdriver, tiene las funciones necesesarias para interactuar con la pagina 
from selenium.webdriver.chrome.service import Service # importamos service para inciar el servicio de chormedriver
from webdriver_manager.chrome import ChromeDriverManager #importa una clase que se encarga de descargar automaticamente el chormedriver correcto 


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#utlizamos los metodos de extracion que tiene by, css selector, xpath, etc 
from selenium.webdriver.common.by import By





# 🔹 ChromeDriverManager().install() - llama al administrador de drivers , descarga si es necesario y devuelve la ruta 
#service = Toma la ruta que devolvio la lina anterior,  inica el servicio para lanzar el navegador correctamente
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.fincaraiz.com.co/venta/casas-y-apartamentos/cucuta/norte-de-santander"  # Reemplaza con la URL de la página que deseas analizar

wait = WebDriverWait(driver, 10)

# driver.get(url) # abrir una pagina
# driver.save_screenshot('foto.png') # tomar captura 



card = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.listingCard.highlight')))
card[0].click()