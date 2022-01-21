'''
Filter -> filter() serve para filtrar dados de uma determinada coleção.

----------------------------------------------------------------

# Biblioteca para trabalhar com dados estatísticos

import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 3.2, 4.7, -0.1]


# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f'Média: {media}')
# Média: 2.3600000000000003

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo uma
# função e um iterável.

res = filter(lambda x: x > media, dados)

print(type(res))
# <class 'filter'>

print(list(res))
# [2.7, 3.2, 4.7]

print(f'Novamente: {list(res)}')
# Novamente: []

# OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são
# excluídos da memória

----------------------------------------------------------------

paises = ['', 'Argentina', 'Brasil', 'Bolivia',
          'Colombia', 'Equador', '', '', '', '']

res = filter(None, paises)

print(list(res))
# ['Argentina', 'Brasil', 'Bolivia', 'Colombia', 'Equador']

res = filter(lambda pais: len(pais) > 0, paises)

print(list(res))
# ['Argentina', 'Brasil', 'Bolivia', 'Colombia', 'Equador']

res = filter(lambda pais: pais != '', paises)

print(list(res))
# ['Argentina', 'Brasil', 'Bolivia', 'Colombia', 'Equador']

----------------------------------------------------------------

# A diferença entre map() e filter() é:
# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função
# para cada elemento iterável.

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas
# os elementos de acordo com a função.

----------------------------------------------------------------

# Exemplo

usuarios = [{'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizza']},
            {'username': 'carla', 'tweets': ['Eu adoro meu gato']},
            {'username': 'jeff', 'tweets': []},
            {'username': 'bob123', 'tweets': []},
            {'username': 'doggo', 'tweets': [
                'Eu gosto de cachorros', 'Vou sair hoje']},
            {'username': 'gal', 'tweets': []}]

# Filtar os usuários que estão inativos no Twitter

# Forma 1
inativo = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

print(inativo)
# [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'gal', 'tweets': []}]

# Forma 2
inativo = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativo)
# [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'gal', 'tweets': []}]


'''

# Comniar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)
# ['Sua instrutora é Ana']