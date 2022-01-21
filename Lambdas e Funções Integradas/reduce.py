'''
Reduce

OBS: A partir o Python3+ a função reduce() não é mais uma função integrada (built-in). Agora temos 
que importar e utilizar está função a partir do módulo 'functools'

Guido van Rossum. Utilize função reduce() se você realmente precisa dela. Em todo caso, 99% das vezes 
um loop for é mais legível.

Para entender o reduce()

# Coleeção de dados:
dados = [a1, a2, a3, ..., an]

def funcao(x, y): 
    return x * y
    
Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o iterável.

reduce(funcao, dados)

A função reduce(), funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o res.

    Isso é repetido até o final.
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn = f(resn, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação. No final, 
reduce() irá retornar o resultado final.

Alternativamente, poderíamos ver a função reduce() como:

funcao(funcao(funcao(aq, a2, a3), a4), ...), an)
'''

from functools import reduce

dados = [1, 2, 4, 5, 10, 20, 30, 40, 50, 60]

# Para utilizar o reduce() nós precisamos de uma função que receba dois parâmetros
multi = lambda x, y: x * y 

res = reduce(multi,dados)

print(res)
# 28800000000

res = 1
for n in dados:
    res = res * n
    
print(res)
# 28800000000