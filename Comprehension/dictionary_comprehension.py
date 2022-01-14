'''
Dictionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista fazemos:
lista = [1, 2, 3, 4, 5, 6, 7, 8]

Se quisermos criar uma tupla:
tupla = (1, 2, 3, 4, 5, 6, 7, 8)

Se quisermos criar um dicionário
dicionario = {'a': 1, 'b': 2, 'c': 3}

# Sintaxe Dictionary Comprehension
{chave:valor for valor in iteravel}

----------------------------------------------------------------

#Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave:valor for chave, valor in numeros.items()}

print(quadrado)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

----------------------------------------------------------------

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

quadrado = {valor: valor ** 2 for valor in numeros}

print(quadrado)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

numeros = [1, 2, 3, 4, 5, 1, 2, 3]

quadrado = {valor: valor ** 2 for valor in numeros}

# Não repete as chaves
print(quadrado)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

----------------------------------------------------------------

chaves = 'abcde'
valores = [1, 2, 3, 4, 5,]

mistura = {chaves[i]:valores[i] for i in range(0, len(chaves))}

print(mistura)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

'''

# Exemplos com lógica condicional

numeros = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}

print(res)
# {1: 'impar', 2: 'par', 3: 'impar', 4: 'par', 5: 'impar'}