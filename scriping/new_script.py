

import requests as r
from bs4 import BeautifulSoup

# Request the page
url = 'https://www.fincaraiz.com.co/venta/casas-y-apartamentos/cucuta/norte-de-santander'
answer = r.get(url)

#Analizate the HTML 
soup = BeautifulSoup(answer.text, 'html.parser') #html.parse, crea un objeto que permite analizar la pagina de manera sencilla 

#Extract Information 

tittles = soup.find_all('h2') # busca y devuelve una lista de todos los elementos h2 


for h1 in tittles:  #recorre todos los h2 encontrados en tittles 
    print(h1.text)