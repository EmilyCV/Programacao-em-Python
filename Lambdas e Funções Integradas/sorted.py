'''
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em listas. O sorte() só 
funciona com listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.

----------------------------------------------------------------

# Exemplo

numeros = [6, 1, 8, 2]

print(sorted(numeros))
# [1, 2, 6, 8]

numeros = (6, 1, 8, 2)

print(sorted(numeros))
# [1, 2, 6, 8]

----------------------------------------------------------------

letras = ('b', 'd', 'a', 'z', 'e')

print(sorted(letras))
# ['a', 'b', 'd', 'e', 'z']

numeros = [6, 1, 8, 2]
# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True))  # Ordena do maior para o menor
# [8, 6, 2, 1]

----------------------------------------------------------------

# Podemos utilizar sorted() para coisas mais complexas

usuarios = [{'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizza']},
            {'username': 'carla', 'tweets': ['Eu adoro meu gato']},
            {'username': 'jeff', 'tweets': []},
            {'username': 'bob123', 'tweets': [], 'cor':'amarelo'},
            {'username': 'doggo', 'tweets': [
                'Eu gosto de cachorros', 'Vou sair hoje']},
            {'username': 'gal', 'tweets': [], 'cor':'preto', 'musica':'rock'}]

print(sorted(usuarios, key=lambda usuario: usuario['username']))
# [{'username': 'bob123', 'tweets': [], 'cor': 'amarelo'}, {'username': 'carla', 'tweets': ['Eu adoro meu gato']}, {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']}, {'username': 'gal', 'tweets': [], 'cor': 'preto', 'musica': 'rock'}, {'username': 'jeff', 'tweets': []}, {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizza']}]

print(sorted(usuarios, key=lambda usuario: usuario['tweets']))
# [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': [], 'cor': 'amarelo'}, {'username': 'gal', 'tweets': [], 'cor': 'preto', 'musica': 'rock'}, {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizza']}, {'username': 'carla', 'tweets': ['Eu adoro meu gato']}, {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']}]

'''

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Black in Black', 'tocou': 4},
    {'titulo': "Too old to rock 'in'roll", 'tocou': 32},
]

print(sorted(musicas, key=lambda musica: musica['tocou']))
# [{'titulo': 'Dead Skin Mask', 'tocou': 2}, {'titulo': 'Thunderstruck', 'tocou': 3}, {'titulo': 'Black in Black', 'tocou': 4}, {'titulo': "Too old to rock 'in'roll", 'tocou': 32}]

print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
# [{'titulo': "Too old to rock 'in'roll", 'tocou': 32}, {'titulo': 'Black in Black', 'tocou': 4}, {'titulo': 'Thunderstruck', 'tocou': 3}, {'titulo': 'Dead Skin Mask', 'tocou': 2}]
