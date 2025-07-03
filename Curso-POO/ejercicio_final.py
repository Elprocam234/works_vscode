
#textblob nos permite extraer informacion importante del texto, procesa datos textuales 
from textblob import TextBlob 

class AnalizadorDeSentimientos: 
    def analizar_sentimientos(self,texto):
        # a textblob vamos a pasarle el texto para que evalue 
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0: 
            return "positivo"
        elif analisis.sentiment.polarity == 0 : 
            return "neutral"
        else: 
            return "negativo"


analizador  = AnalizadorDeSentimientos()
resultado = analizador.analizar_sentimientos("hola como estas")
print(resultado)