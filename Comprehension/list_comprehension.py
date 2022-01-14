'''
List Comprehension - Nós podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe da List Comprehension
[dado for dado in iteravel]

----------------------------------------------------------------

# Exemplos

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

res = [numero * 10 for numero in numeros]

print(res)
# [10, 20, 30, 40, 50, 60, 70, 80]

"""
Devemos dividir a expressão em duas partes:
- A primeira parte: for numero in numeros
- A segunda parte: numero*10
"""

res = [numero/2 for numero in numeros]

print(res)
# [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]


def funcao(valor):
    return valor*valor

res = [funcao(numero) for numero in numeros]

print(res)
# [1, 4, 9, 16, 25, 36, 49, 64]

----------------------------------------------------------------

# List Comprehension versão Loop

# Loop

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero*2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)
# [2, 4, 6, 8, 10, 12, 14, 16]

# List Comprehension

print([numero*2 for numero in numeros])
# [2, 4, 6, 8, 10, 12, 14, 16]

'''

# Exemplos

# 1

nome = 'Geek University'

print([letra.upper() for letra in nome])
# ['G', 'E', 'E', 'K', ' ', 'U', 'N', 'I', 'V', 'E', 'R', 'S', 'I', 'T', 'Y']

# 2


def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([caixa_alta(amigo) for amigo in amigos])
# ['Maria', 'Julia', 'Pedro', 'Guilherme', 'Vanessa']

# 3

print([numero*3 for numero in range(1, 10)])
# [3, 6, 9, 12, 15, 18, 21, 24, 27]

# 4

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])
# [False, False, False, True, True, True]

# 5

print([str(numero) for numero in [1, 2, 3, 4, 5]])
# ['1', '2', '3', '4', '5']
