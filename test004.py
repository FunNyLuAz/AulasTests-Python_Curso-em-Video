#(Ctrl+Space, para mostrar todas as funções possíveis)
#Importação Generalizada
import math

n = int(input('Digite um número: '))
r = math.sqrt(n)
print('A raiz quadrada é:', r)
print('A raiz quadrada é:', math.ceil(r))
print('A raiz quadrada é:', math.floor(r))

#Importação Específica
#from math import ###


import random
nn1 = random.random()#Número real aleatório entre 0 e 1
print(nn1)

nn2 = random.randint(1,12)#Número inteiro aleatório entre 1 e 12
print(nn2)

import emoji
print(emoji.emojize('Bom dia :smile:', use_aliases=True))
