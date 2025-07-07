#indice de masa corporal con clases 


class Person:
    def __init__(self, name,weight, height):
        self.name = name 
        self.weight = weight
        self.height = height
        




class Evaluation(Person):
    #generamos metodo constructor 
    def __init__(self, name, weight, height):
        #heredamos de class Person and Category 
        Person.__init__(self,name, weight, height)
        
        self.evalue = self.weight / (self.height**2)
    #obtnemos el estado de la persona
    # atributo dinamico 
    def get_status(self): 
        if 18.5 <= self.evalue  <=  24.9: 
            return 'good'
        elif 25 <= self.evalue <= 29.9:
            return 'bad'
        else : 
            return 'otro'

class Category(Evaluation):
    def __init__(self, name, weight, height): 
        super().__init__(name, weight, height)
    
    def check_status(self): 
        status = self.get_status()
        if status == 'good'.lower() : 
            print(f'Tu indice es de {self.evalue } y estas bien')
        elif status == 'bad'.lower(): 
            print(f'Tu indice es de {self.evalue } y estas mal')
        else : 
            print(f'Tu indice es de {self.evalue } y no sabemos como estas ')
    
        
            
        
    
    
    
name = input('Coloque su nombre: ')
weight = int(input('Coloque su peso: '))
height = int(input('Coloque su altura: '))

pedro = Category(name, weight, height)
pedro.check_status()



