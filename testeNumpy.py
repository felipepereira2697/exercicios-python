import numpy as np

#Para o numpy executar corretamente, devemos garantir que os tipos nas listas são iguais
alturas = [1.77,1.61, 1.66,1.65]
pesos = [75,50, 74,75]
np_alturas = np.array(alturas)
np_pesos = np.array(pesos)

imc = np_pesos/np_alturas ** 2

print(f'O imc dos dados passados estão na seguinte ordem: {imc} ')

#Diferença entre somar duas listas

#Python regular
lista = [1,2,3]

print(f'Soma de listas no python regular {lista+lista}')

#usando NumPy
np_array = np.array(lista) 
print(f'Soma de listas com numpy {np_array+np_array}')

#Imagine que queremos pegar todos os elementos de uma lista que tenham valor igual a 75
print(np_pesos > 74)
print(np_pesos[np_pesos > 74])
