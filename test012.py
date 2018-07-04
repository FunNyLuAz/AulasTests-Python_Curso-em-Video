#Listas são mutáveis
n = [5, 6, 2, 5]
p = ['Lucas', 14, 52.4, 1.62]
n[2] = 4
print(n)

#Adicionar valores:
'''n[4] = 9 (Dá erro)
n += [9] or n.append(9) (No final da lista)
n.insert(2, 5) (Em posição específica, não apagando nenhum elemento, apenas o empurrando para frente)'''

#Organizar listas:
'''n.sort() (Modo normal)
print(n)
n.sort(reverse=True) (Modo ao contrário)
print(n)'''

#Contar elementos:
'''print(len(n))'''

#Deletar elementos:
'''n.pop() (Deleta o último elemento)
n.pop(2) (Especificado, deleta o elemento a sua escolha (Posição))
del n[2] (Deleta um elemento especificado (Posição))
p.remove('Lucas') (Busca e deleta o elemento mencionado (Não funciona com Posição)) 
n.remove(5) (Apenas a primeira ocorrência, caso haja mais de uma)
n.remove(9) (Dá erro, caso o elemento não esteja na lista, para evitar esse erro use:
   {"if 9 in n:
       n.remove(9)"})'''

#Criação de lista vazias:
'''m = []
m = list()'''

#Remover "[]" e ",":
'''for c in n:
    print(f'{c}...') (Sem Índice)
for ct, c in enumerate(n):
    print(f'{c} em {ct}...') (Com índice)'''

#Adicionar muitos valores:
'''for t in range(0, 5):
    n.append(int(input('Digite um valor: ')))
for t in range(0, 5):
    n += [int(input('Digite um valor: '))]'''

#Ligação entre Listas:
'''a = [2, 3, 4]
b = a (Você vincula uma lista na outra, e não copia)
b[2] = 8'''

#Cópia de Lista, sem ligação:
'''a = [2, 3, 4]
b = a[:] (Você apenas copia e não vincula uma lista na outra)
b[2] = 8'''

