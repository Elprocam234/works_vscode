from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configura el navegador
driver = webdriver.Chrome()  # driver será el encargado de controlar el navegador 
driver.get("https://www.fincaraiz.com.co/venta/casas-y-apartamentos/cucuta/norte-de-santander")

# Esperar que aparezca el enlace de la tarjeta y hacer clic
wait = WebDriverWait(driver, 15)
enlace = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.listingCard.highlight a.lc-cardCover')))
enlace.click()
print("URL actual:", driver.current_url)
# Esperar que cargue la nueva página después del clic
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.property-typology-tag-desktop span.ant-typography-ellipsis")))

# Buscar todos los span con esa clase específica
spans = driver.find_elements(By.CSS_SELECTOR, "div.property-typology-tag-desktop span.ant-typography-ellipsis")

# Imprimir el texto de cada span encontrado
for span in spans: 
    print(span.text)
