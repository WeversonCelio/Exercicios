'''Exercícios'''
##Crie uma lista com o nome das 3 pessoas mais próximas.
nomes = ['ana', 'maria', 'paulo']

##Crie três listas, uma lista de cada coisa a seguir:
## frutas
frutas = ['maça','manga','banana']
##docinhos de festa
doces = ['brigadeiros','beijinho','bolo']
## ingredientes de feijoada
feijoada = ['feijao', 'calabresa', 'porco']

##a. Agora crie uma lista que contém essas três listas.
listona = frutas + doces + feijoada
print(listona)

##Nessa lista de listas (vou chamar de listona):
##b. você consegue acessar o elemento brigadeiro?
print('brigadeiros' in listona)

##c. Adicione mais brigadeiros à segunda lista de listona.
##O que aconteceu com a lista de docinhos de festa?
listona.append('brigadeiros')
print(doces)
##d. Adicione bebidas ao final da listona, mas sem criar uma lista!
listona = listona + ['cerveja', 'refrigerante', 'vinho']
print(listona)
##Utilizando ou excluindo, remova todos os elementos da lista criada anteriormente até a lista ficar vazia.
del listona[-1]

##Dado uma lista de números, faça com que os números sejam ordenados e, em seguida, inverta uma ordem da lista usando o fatiamento.
numero = [10, 5, 7, 11]
numero.sort()
print(numero)
print(numero[-1:])
