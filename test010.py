c = 0
while c < 10:
    print(c, end='')
    c += 1

r = 'S'
while r == 'S':
    n = int(input('\nDigite um valor: '))
    r = input('Quer continuar? (S/N)').capitalize()

#Interupções do while
ct = 0
while True:
    nj = int(input('Digite um valor: '))
    if nj == 999:
        break
    ct += nj
print(ct)

#Atualização (f.str)
print('A soma vale {}'.format(ct))
print(f'A soma vale {ct}')
