'''
Generators -> Tuple Comprehension

------------------------------------------------------------------------------

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))
# True

------------------------------------------------------------------------------

# Generators
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))
# True

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]

print(type(res))
# <class 'bool'>

print(res)
# [True, True, True, True, False]

# Generator
res = (nome[0] == 'C' for nome in nomes)

print(type(res))
# <class 'generator'>

print(res)
# <generator object <genexpr> at 0x0000022A1E481F50>

----------------------------------------------------------------

# getsizeof() -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' está ocupando de memória.
print(getsizeof('Geek'))
# 53

print(getsizeof('University'))
# 59

print(getsizeof(9))
# 28

print(getsizeof(True))
# 28

----------------------------------------------------------------


from sys import getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x*10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x*10 for x in range(1000)})

# Gerando uma lista de números com Dicionary Comprehension
dic_comp = getsizeof({x: x*10 for x in range(1000)})


# Gerando uma lista de números com Generator
gen = getsizeof(x*10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp}')
# List Comprehension: 8856

print(f'Set Comprehension: {set_comp}')
# Set Comprehension: 32984

print(f'Dicionary Comprehension: {dic_comp}')
# Dicionary Comprehension: 36960

print(f'Generator: {gen}')
# Generator: 104


'''

gen = (x*10 for x in range(1000))
print(gen)
# <generator object <genexpr> at 0x000002456DF61F50>

print(type(gen))
# <class 'generator'>

for num in gen:
    print(num)
