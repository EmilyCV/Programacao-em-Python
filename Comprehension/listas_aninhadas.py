'''
Listas Aninhadas

- Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores); 
    - Multidimensionais(Matrizes);

Em Python nós temos as listas

----------------------------------------------------------------

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3

print(listas)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(type(listas))
# <class 'list'>

# Como fazemos para acessar os dados?

print(listas[0][1])
# 2

# Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)

# List Comprehension
[[print(valor) for valor in lista] for lista in listas]


'''

# Gerando um tabuleiro/matriz 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]

print(tabuleiro)

# Gerando jogadas para o jogo da velha

velha = [['X' if numerp % 2 == 0 else '0' for numerp in range(
    1, 4)] for valor in range(1, 4)]

print(velha)
# [['0', 'X', '0'], ['0', 'X', '0'], ['0', 'X', '0']]

# Gerando valores iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])
# [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
