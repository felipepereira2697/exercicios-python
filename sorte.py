from random import randint
choice = randint(1,10)

if choice == 7:
    print(f'Tirou a sorte grande, número {choice}')
else:
    print(f'Não tirou a sorte grande, número selecionado {choice}')