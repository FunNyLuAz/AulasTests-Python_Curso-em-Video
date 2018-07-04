#Manipulação de Texto
f = 'Curso em Vídeo Python'

print('Sua frase tem', len(f), 'caracteries')

print('Sua frase tem', f.count('o'), 'letras o')

print('Sua frase tem', f.count('o', 0, 14), 'letras o entre 0 e 14')

print('O deo apareceu primerio no índice', f.find('deo'))

print('Existe Curso dentro da frase?', 'Curso' in f)

print('Substituindo Python por CC+ temos:', f.replace('Python', 'CC+'))

print('Deixando tudo em maiúsculo temos:', f.upper())

print('Deixando tudo em maiúsculo temos:', f.lower())

print('Deixando tudo capitalizado temos:', f.capitalize())

print('Deixando tudo como em título temos:', f.title())

s = '   Aprenda Python     '

print('Apagando os espaços excedentes temos:', s.strip())

print('Apagando os espaços excedentes da direita temos:', s.rstrip())

print('Apagando os espaços excedentes da esquerda temos:', s.lstrip())

#Divisão de Texto
print('Dividindo seu texto de acordo com os espaços temos:', f.split())

print('Adicionando - entre as palavras temos:', '-'.join(f.split()))
