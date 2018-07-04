#Tuplas são imutáveis

#Modo antigo (Tupla) - FUNCIONA
l = ('h', 's', 'pi', 'pu')

#Modo atual (Tupla) - FUNCIONA
l = 'h', 's', 'pi', 'pu'

print(l)
print(l[1])
print(l[2:])
print(l[-2])
print(l[1:3])
print(l[0:2])
print(l[-2:])

for c in l:
    print(c, end=' ')

print('\n')
#Resultado igual nos dois
for ct, c in enumerate(l):
    print(f'{c} na pos {ct}', end=' ')
print('\n')
for c in range(0, len(l)):
    print(f'{l[c]} na pos {c}', end=' ')

print('\n')
print(len(l))

#Organizado
print(sorted(l))

#Junção de tuplas em uma tupla
a = (2, 5, 4)
b = (3, 5, 8, 1)

c = a + b
print(c)

c = b + a
print(c)


print(c.count(5))

#Função index (Posição da primeira aparição)
print(c.index(5))

#Função index (Posição da primeira aparição, apartir da posição 3)
print(c.index(5, 3))

#Tuplas podem receber int, str, etc...
p = ('Lucas', 14, 1.62, 53, 'M')

#É possível apagar tuplas
del p
#print(p)
