# Vamos construir o jogo de pedra papel e tesoura
print('Seja bem vindo ao PedraPapelTesoura')
print('-------------------------------------')

jogador1 = input("Pedra, papel ou tesoura?")
print('-------------------------------------')
print('-------------------------------------')
print('-------------------------------------')
print('--------------SEM ROUBAR--------------------')
print('-----------SEM ROUBAR-------------')
print('---SEM ROUBAR----------------------------')
print('-------------------------------------')
print('-------------------------------------')
jogador2 = input("Jogador 2, pedra, papel ou tesoura? ")
print('-----------------------------------')
print('-----------------------------------')
print('---------------3, 2, 1 eeeee....')
print('VAI!')

if jogador1 == 'pedra' and jogador2 == 'tesoura' :
    print(f'No duelo do século quem venceu foi quem escolheu {jogador1} !!  Parabéns! ')  
elif jogador1 =='pedra' and jogador2 =='pedra':
    print(f'EMPATOU! VAMOS JOGAR NOVAMENTE')
else:
        print('')

    