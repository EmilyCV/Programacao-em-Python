'''
Named Tuple -> São Tuplas, diferenciadas, onde, especificamos um nome para a mesma  e também parâmetros.

'''

from collections import namedtuple

# Precisamos definir o nome e parâmetros

# Forma 1 - Declarção Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando
ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

print(ray)
# cachorro(idade=2, raca='Chow-Chow', nome='Ray')

# Acessando dados
# Forma 1

print(ray[0])
# 2
print(ray[1])
# Chow-Chow
print(ray[2])
# Ray

# Forma 2

print(ray.idade)
# 2
print(ray.raca)
# Chow-Chow
print(ray.nome)
# Ray

print(ray.index('Chow-Chow'))
# 1
print(ray.count('Chow-Chow'))
# 1
