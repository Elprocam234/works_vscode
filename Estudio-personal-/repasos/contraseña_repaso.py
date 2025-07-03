
import random 

def contraseña(): 
    num = input(f'Ingresa un numero para crear tu clave: ')
    num_entero = int(random.choice(num))
    ch = 'abcdefghijklmnopqrst'
    c1 = ch[num_entero - 1] 
    c2 = ch[num_entero + 1] 
    password  = f'{c1}{c2}{num_entero*2}'
    return password,num

contra,num = contraseña()
print(f'{contra}{num}')