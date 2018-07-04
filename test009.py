for c in range(0, 5): #Repetição
    print('Olá')
print('Fim')

for c in range(1, 6): #Contagem
    print(c)

for c in range(5, 0): #Contagem de trás para frente (Não Funciona)
    print(c)

for c in range(5, 0, -1): #Contagem de trás para frente (Funciona)
    print(c)

for c in range(5, 0, -1): #Contagem de trás para frente (Funciona)
    print(c)

for c in range(0, 6, 2): #Contagem pulando de 2 em 2
    print(c)

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)

n1 = int(input('Digite o começo: '))
n2 = int(input('Digite o fim: '))
n3 = int(input('Digite o passo: '))
for c in range(n1, n2+1, n3):
    print(c)

for c in range(0, 3): #Repetir comandos Ex.:INPUT
    t = input('Digite um valor: ')

s = 0
for y in range(0, 3): #Repetir comandos Ex.:INPUT
    t = int(input('Digite: '))
    s += t
print('A soma entre eles é', s)
