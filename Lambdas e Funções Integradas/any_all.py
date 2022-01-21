'''
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

# Exemplo all()

print(all([0, 1, 2, 3, 4, 5]))  # Todos os números são verdadeiros?
# False

print(all([1, 2, 3, 4, 5]))
# True

print(all([]))
# True

print(all('Geek'))
# True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristiana']

print(all(nome[0] == 'C' for nome in nomes))
# True

print(all(letra for letra in 'elo' if letra in 'aeiou'))
# True

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))
# True

-------------------------------------------------------------------------------

any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
'''

print(any([0, 1, 2, 3, 4, 5]))
# True

print(any([0, False, {}, 3, 4]))
# True

print(any([0, False, {}, (), []]))
# False

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristiana']

print(any([nome[0] == 'C' for nome in nomes]))
# True

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))
# True