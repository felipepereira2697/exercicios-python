from random import randint
num = randint(1,1000)
if num%2 != 0:
    print(f'Número {num} é ímpar')
else:
    print(f'Número {num} é par')