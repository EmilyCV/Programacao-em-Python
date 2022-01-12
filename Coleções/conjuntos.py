"""
Conjuntos
- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos da Mátematica

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, dda mesma forma que na mátemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para utilizar quando precisamos armazenar elementos, mas não nos importamos com a ordenação deles.
Quando não precisamos nos preocupar com chaves, valores e itens duplicadps.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Set) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

----------------------------------------------------------------

# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 7, 7, 2, 3})
print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existe, o mesmo será ignorado
# sem gerar erros e não fará parte do conjunto.

# Forma 2

s = {1, 2, 3, 4, 5, 5, 7, 7, 2, 3}
print(s)
print(type(s))

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

----------------------------------------------------------------

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas e Tuplas aceitam valores duplicados

lista = [99, 2, 34, 23, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

tupla = (99, 2, 34, 23, 12, 1, 44, 5, 34)
print(f'Tupla: {lista} com {len(tupla)} elementos')

# Dicionários não aceitam chaves duplicadas

dicionario = {}.fromkeys(lista, 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados
conjunto = {99, 2, 34, 23, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

----------------------------------------------------------------

# Assim como todo outo conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}

#Podemos iterar em um set normalmente
for valor in s:
    print (valor)

----------------------------------------------------------------

# Formulário de cadastro de visitantes
# informando manualmente a cidade

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande',
           'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Quantas cidades distintas (únicas)
print(len(set(cidades)))

----------------------------------------------------------------

# Adicionando elementos em um conjunto
s = {1, 2, 3}

s.add(4)
s.add(4)
print(s)

----------------------------------------------------------------

s = {1, 2, 3}
print(s)

# Forma 1

s.remove(3)
print(s)

# OBS: Caso o valor não seja encontrado será gerado o erro KeyError. Nenhum valor é retornado

# Forma 2

s.discard(22)
print(s)

# OBS: Se o valor não for encontrado, nenhum erro ée gerado

----------------------------------------------------------------

#Copiando um conjunto para outro

s = {1, 2, 3}

# Forma 1 - Deep Compy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow copy
novo = s

novo.add(4)

print(novo)
print(s)

"""

# Métodos mátematicos de Conjuntos
# Imagine que temos dois conjuntos: Um contendo estudantes do curso de Python e um contendo
# estudantes do curso de Java.

estudantes_python = {'Marcos', 'Patricia',
                     'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando',  'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Conjuntos com nomes de estudantes únicos

# Forma 1 - Utilizando union

unicos1 = estudantes_java.union(estudantes_python)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe |

unicos2 = estudantes_java | estudantes_python
print(unicos2)

# Gerando um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes que não estão no mesmo curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma*, Valor Máximo*, Valor Mínino*, Tamanho
# *Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
