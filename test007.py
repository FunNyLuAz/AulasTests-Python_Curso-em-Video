n = input('Qual é o seu nome?: ')

if n == 'Lucas':
    print('Olá Lucas')
else:
    print('Bom dia')
print('Bem-vindo')


if n == 'Ricardo':
    print('Oi Ricardo, que nome lindo')
print('Tudo bem?')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
ns = (n1 + n2)/2
print('Sua média é:', ns)
if ns >= 6.0:
    print('Parabéns pela sua média')
else:
    print('Estude mais na próxima vez')

#Módulo 'Time'
import time
time.sleep(3) #Pausa o computador por um tempo (segundos)

#Módulo 'DateTime'
import datetime
datetime.date.today().year #Mostra o ano atual

#Cores - ANSI
#\033[m
#Style, Color, Color Back
#Print com o os códigos
