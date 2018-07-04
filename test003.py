print(5+2)
print(5-2)
print(5*2)
print(5**2)
print(5/2)
print(5//2)
print(5%2)

#5**2
print(pow(5,2))

print(81**(1/2))

print(27**(1/3))

print(16**(1/4))

print('Oi'+'Olá')
print('Oi'*5)

a = input('Nome: ')
print('Olá {}!'.format(a))
print('Olá {:20}!'.format(a))
print('Olá {:>20}!'.format(a))
print('Olá {:<20}!'.format(a))
print('Olá {:^20}!'.format(a))
print('Olá {:_^20}!'.format(a))
print('Olá {:=^20}!'.format(a))

n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
print('A soma é {}'.format(n1+n2))

so=n1+n2
sb=n1-n2
m=n1*n2
d=n1/n2
p=n1**n2
di=n1//n2
rd=n1%n2

print('A soma é {}, a subtração é {}, a multiplicação é {} e a divisão é {}'.format(so,sb,m,d))
print('A poteciação é {}, a divisão inteira é {} e o resto da divisão é {}'.format(p,di,rd))

nn1=int(input('Digite uma equação divisível irracional (Número 1):'))
nn2=int(input('Digite uma equação divisível irracional (Número 2):'))

nn3=nn1/nn2

print('O Resultado de {} dividido por {} é:{}'.format(nn1,nn2,nn3))
print('O Resultado de {} dividido por {} é:{:.4f}'.format(nn1,nn2,nn3))
print('O Resultado de {} dividido por {} é:{:.1f}'.format(nn1,nn2,nn3))

print('O Rato roeu a roupa',end='')
print(' do rei de Roma')

print('O Rato roeu a roupa',end=' do rei')
print(' de Roma')

print('O Rato roeu\n a roupa do rei\n de Roma')
