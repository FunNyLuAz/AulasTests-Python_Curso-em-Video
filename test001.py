n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
s = n1 + n2
print(s)

b1 = float(input('Digite um número: '))
b2 = float(input('Digite um número: '))
c = b1 + b2
print(c)

print(type(n1))
print(type(n2))
print(type(b1))
print(type(b2))

print('A soma entre', n1, 'e', n2, 'é', s)
print('A soma entre', b1, 'e', b2, 'é', c)

print('A soma entre {} e {} é {}'.format(n1, n2, s))
print('A soma entre {} e {} é {}'.format(b1, b2, c))
