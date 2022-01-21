'''
Zip

zip() -> Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares.

----------------------------------------------------------------


# Exemplos
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]

zip1 = zip(lista1, lista2)

zip2 = zip(lista1, lista2, "abc")

print(zip1)
# <zip object at 0x0000025D5C6A7140>

print(type(zip1))
# <class 'zip'>

# Sempre podemos gerar uma Lista, Tupla ou Dicionário

print(list(zip1))
# [(1, 5), (2, 6), (3, 7), (4, 8)]

print(list(zip2))
# [(1, 5, 'a'), (2, 6, 'b'), (3, 7, 'c')]

print(tuple(zip1))
# ()

print(set(zip1))
# set()

print(dict(zip1))
# {}

# ----------------------------------------------------------------

# Para funcionar seria necessário executar novamente, pois some da memória
zip1 = zip(lista1, lista2)
print(tuple(zip1))
# ((1, 5), (2, 6), (3, 7), (4, 8))

zip1 = zip(lista1, lista2)
print(set(zip1))
# {(3, 7), (2, 6), (4, 8), (1, 5)}

zip1 = zip(lista1, lista2)
print(dict(zip1))
# {1: 5, 2: 6, 3: 7, 4: 8}


# OBS: O zip() utiliza como parâmetro o menos tamanho em iterável. Isso significa que se estiver
# trabalhando com iteráveis de tamanhos diferentes, irá parar quando os elementos do menor
# iterável acabar.

lista3 = [9, 10, 11, 12, 13]
zip1 = zip(lista1, lista2, lista3)

print(list(zip1))
# [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

----------------------------------------------------------------

# Podemos utilizar diferentes iteráveis com zip

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15, 'f': 16}

zt = zip(tupla, lista, dicionario.values())

print(list(zt))
# [(1, 1, 11), (2, 2, 12), (3, 3, 13), (4, 4, 14), (5, 5, 15), (6, 6, 16)]

# Lista de Tuplas

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

# * -> Usado para desempacotar
print(list(zip(*dados)))
# [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]

'''

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0].capitalize(): max(dado[1], dado[2])
         for dado in zip(alunos, prova1, prova2)}

print(final)
# {'maria': 98, 'pedro': 91, 'carla': 78}

# Podemos utilizar o map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))
# {'maria': 98, 'pedro': 91, 'carla': 78}