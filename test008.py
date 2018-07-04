n = input('Digite seu nome: ')

# O IF é obrigatório
if n == 'Lucas':
    print('Que nome legal!')
# O ELIF é opcional e ilimitado
elif n in 'Gustavo Paula Roberto Ricardo':
    print('Nome interresante, {}'.format(n))
# O ELSE é opcional e limitado
else:
    print('Você tem um nome bem normal')

print('Tenha um bom dia, {}'.format(n))
