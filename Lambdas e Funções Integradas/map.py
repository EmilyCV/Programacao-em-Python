'''
Map -> Fzemos mapeamento de valores para função.

----------------------------------------------------------------

import math


def area(r):
    """ Calcula a área de um círculo com raio 'r'."""
    return math.pi * (r**2)


print(area(2))
# 12.566370614359172

print(area(5.3))
# 88.24733763933729

raios = [2, 5, 7.1, 0.3, 10, 44]

# Froma comum
areas = []

for r in raios:
    areas.append(area(r))

print(areas)
# [12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793, 6082.12337734984]

# Forma 2 - Mapas

# Map é uma fução que recebe dois parâmetros: O primeiro a função, o segundo um iterável
areas = map(area, raios)

print(areas)
# <map object at 0x00000210ADC4BF10>

print(type(areas))
# <class 'map'>

print(list(areas))
# [12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793, 6082.12337734984]

# Forma 3 - Map com Lambda

print(list(map(lambda r: math.pi * (r**2), raios)))
# [12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793, 6082.12337734984]

# OBS: Após utilizar a função map() a lista é zerada.

----------------------------------------------------------------

# Temos dados iteráveis

# dados: a1, a2, ..., anônimas

# Temos uma função:

# Função: f(x)

# Utilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função.

# O Map  Object: f(a1), f(a2), f(...), f(an)

'''

# Mais exemplos

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19),
           ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Lodres', 22)]

print(cidades)

# f = 9/5 * c + 32

# Lambda


def c_para_f(dado): return (dado[0], (9/5*dado[1]+32))


print(list(map(c_para_f, cidades)))
# [('Berlim', 84.2), ('Cairo', 96.8), ('Buenos Aires', 66.2), ('Los Angeles', 78.80000000000001), 
# ('Tokio', 80.6), ('Nova York', 82.4), ('Lodres', 71.6)]
