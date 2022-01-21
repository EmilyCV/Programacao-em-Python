'''
Reversed

OBS: Não confunda com a função reverse()

A função reverse() só funciona com listas.

Ja a função reversed() funciona com qualquer iterável.

Sua função é inverter o iterável.

A função reverserd() retorna um iterável chamado List Reverse Iterator
'''

# Exemplos

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

res = reversed(lista)

print(res)
# <list_reverseiterator object at 0x000001D48089B1C0>

print(type(res))
# <class 'list_reverseiterator'>

# Podemos converter o elemento retornado para uma Lista, Tupla ou Conjunto

# Lista

print(list(reversed(lista)))
# [9, 8, 7, 6, 5, 4, 3, 2, 1]

# Tupla

print(tuple(reversed(lista)))
# (9, 8, 7, 6, 5, 4, 3, 2, 1)

# Conjunto (Set)
# OBS: Em conjuntos, não definimos a ordem dos elementos
print(set(reversed(lista)))
# {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Podemos iterar sobre o reversed
for letra in reversed("Geek University"):
    print(letra, end="")
    # ytisrevinU keeG

# Podemos fazer o mesmo sem o uso do for
'''
O método join() é um método de string e retorna uma 
string na qual os elementos da sequência foram unidos por um separador str.

Ex:

list1 = ['g', 'e', 'e', 'k', 's'] 
 
print("".join(list1))
# geeks
'''
print("".join(list(reversed("Geek University"))))
# ytisrevinU keeG


# Já vimos como fazer isso mais fácil com o slice de string
print("Geek University"[::-1])
# ytisrevinU keeG

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

# Apesar que também já vimos como fazer isso utilizando o próprio range()
for n in range(9, -1, -1):
    print(n)
