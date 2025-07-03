def contraseña_aleatoria():
    import random
    num = input('Digite un numero para elegir su nueva clave : ')
    num = int(random.choice(num)) #toma un valor aleatorio 
    ch = 'abcdefghijklmñopqrstuvwxyz'
    c1 = ch[num-1]
    c2 = ch[num - 2]
    c3 = ch[num] 
    password = f'{c1}{c2}{c3}{num*2}'
    return password,num

contri,num = contraseña_aleatoria()
print(f'{contri}{num}')
