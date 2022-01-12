"""
Collections - Counter

Collections -> High-performance Container Datatypes

Counter -> Recebe um interável como paramêtro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade 
de ocorrências desse elemento.

----------------------------------------------------------------

# Utilizando o Counter

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iterável
lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4,
         4, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

res = Counter(lista)
print(type(res))
print(res)

# Counter({3: 4, 1: 3, 2: 3, 4: 3, 5: 3, 45: 2, 66: 2, 43: 1, 34: 1})
# Para cada elemento da lista o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

----------------------------------------------------------------

# Exemplo 2

from collections import Counter

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

"""
# Exemplo 3

from collections import Counter

texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua. Mattis pellentesque id nibh tortor id. Mi bibendum neque egestas congue quisque 
egestas diam in. Pellentesque adipiscing commodo elit at imperdiet dui accumsan sit amet. Ac turpis egestas sed 
tempus urna et pharetra pharetra massa."""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)
'''Counter({'egestas': 3, 'sit': 2, 'adipiscing': 2, 'sed': 2, 'et': 2, 'pharetra': 2, 'Lorem': 1, 'ipsum': 1, 'dolor': 1, 'amet,': 1, 'consectetur': 1, 'elit,': 1, 'do': 1, 'eiusmod': 1, 'tempor': 1, 'incididunt': 1, 'ut': 1, 'labore': 1, 'dolore': 1, 'magna': 1, 'aliqua.': 1, 'Mattis': 1, 'pellentesque': 1, 
'id': 1, 'nibh': 1, 'tortor': 1, 'id.': 1, 'Mi': 1, 'bibendum': 1, 'neque': 1, 'congue': 1, 'quisque': 1, 'diam': 1, 'in.': 1, 'Pellentesque': 1, 'commodo': 1, 'elit': 1, 'at': 1, 'imperdiet': 1, 'dui': 1, 'accumsan': 1, 'amet.': 1, 'Ac': 1, 'turpis': 1, 'tempus': 1, 'urna': 1, 'massa.': 1})'''

# Encontrando as 5 palavras com mais ocorrências no texto
print(res.most_common(5))
# [('egestas', 3), ('sit', 2), ('adipiscing', 2), ('sed', 2), ('et', 2)]
