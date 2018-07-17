#Estrutura Composta:
'''test = list()
test.append('Gustavo')
test.append(40)
print(test)'''

#Estrutura Composta dentro de outra Estrutura:
'''test = list()
galera = list()
test.append('Gustavo')
test.append(40)
galera.append(test[:])
print(galera)'''

#Estrutura Composta dentro de outra Estrutura (Ligação):
'''test = list()
galera = list()
test.append('Gustavo')
test.append(40)
galera.append(test) (Para não criar a ligação, apenas coloque [:] depois de test, criando uma cópia)
test[0] = 'Maria'
test[1] = 22
print(galera)'''

#Estrutura Composta dentro de outra Estrutura (Sem Ligação/Adicionar Elementos com mesma origem(test)):
'''test = list()
galera = list()
test.append('Gustavo')
test.append(40)
galera.append(test[:])
test[0] = 'Maria'
test[1] = 22
galera.append(test[:])
print(galera)'''

#Declarando listas com dados/Se refirir a determinados dados dentro dela
'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])

for pessoa in galera:
    print(pessoa)
for pessoa in galera: #Apenas os nomes
    print(pessoa[0])
for pessoa in galera: #Apenas as idades
    print(pessoa[1])
for pessoa in galera: #Dados das pessoas formatados
    print(f'{pessoa[0]} tem {pessoa[1]} anos')'''

#Requerimentos de Dados:
'''galera = []
pessoa = []

for c in range(0, 3):
    pessoa.append(str(input('Digite o nome: ')))
    pessoa.append(int(input('Digite a idade: ')))
    galera.append(pessoa[:])
    pessoa.clear() #Utilizado para apagar listas
print(galera)'''

#Filtrando Dados:
'''galera = []
pessoa = []
mai = men = 0

for c in range(0, 3):
    pessoa.append(str(input('Digite o nome: ')))
    pessoa.append(int(input('Digite a idade: ')))
    galera.append(pessoa[:])
    pessoa.clear() #Utilizado para apagar listas

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        mai += 1
    else:
        print(f'{p[0]} é menor de idade')
        men += 1
print(f'O total de maiores é de {mai} pessoa(s), e de menores é de {men} pessoa(s)')'''
