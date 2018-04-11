#Classificar a comida
from random import choice

comida = choice(['maça','Banana', 'bacon', 'picanha', 'minhoca', 'sujeira'])
if comida == 'Maca' or comida == 'banana':
    print(f'{comida} faz bem!')
elif comida == 'bacon' or comida == 'picanha':
    print(f'Hmmmm {comida}!!')
else:
    print(f'Ai não dá né você escolheu {comida} ')

