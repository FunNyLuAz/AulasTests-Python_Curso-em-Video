#Manipulando Texto
f = 'Curso em Vídeo Python'

print('O segundo caractere é:', f[2])

print('Do segundo caractere ao quarto fica:', f[2:5])

print('Do primeiro caractere ao quarto fica:', f[:5])#ou f[0:5]

print('Do terceiro caractere ao último fica:', f[3:])#ou f[3:21]

print('Do segundo caractere ao décimo sexto, pulando de 2 em 2 fica:', f[2:16:2])

print('Do começo ao fim, pulando de 2 em 2 fica:', f[::2])#ou f[0:21:2],f[:21:2],f[0::2]

#Escrever textos
print("""Os desafios que enfrentamos são reais. Eles são sérios e
são muitos. Eles não serão encarados com facilidade ou num curto
período de tempo. ...-Barack Obama""")

#Letras minúsculas se diferem de maiúsculas

#Combinando
print('Esta frase, caso colocado tudo em maiúsculo temos:', f.upper().count('O'), 'O maiúsculos')

s = '   Aprenda Python     '

print('Contando com e sem espaços, temos:\nCom:{}\nSem:{}'.format(len(s), len(s.strip())))

print('Contando sem e com reposicionamento, temos:\nSem:{}\nCom:{}'.format(len(f), len(f.replace('Python', 'Android'))))

print('Esta frase, caso colocado tudo em minúsculo tem na posição {} o começo da palavra vídeo'.format(f.lower().find('vídeo')))

print('Mostrando a segunda letra da terceira palavra, ficamos com:', f.split()[2][1])
