#O objetivo desse exercicio é receber o input do usuário e converter de quilometros para milhas
print('Quantos quilômetros você percorreu hoje?')
km = input()
umaMilha = 1.60934
totalMilhas = float(km)/umaMilha
totalMilhas = round(totalMilhas,2)

print(f'Uau bastante coisa em, não é todo mundo que aguenta {totalMilhas} milhas! Parabéns! ')  