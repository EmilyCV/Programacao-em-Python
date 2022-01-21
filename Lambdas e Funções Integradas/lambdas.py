'''
Lambdas - São funções em nome, ou seja, funções anônimas.

--------------------------------------------------------------

# Exemplo
lambda x: 3*x + 1

calc = lambda x: 3*x + 1

print(calc(4))
# 13

--------------------------------------------------------------

# Podemos ter expressões lambdas com múltiplas enntradas


def nome_completo(nome, sobrenome): return nome.strip(
).title() + ' ' + sobrenome.strip().title()


print(nome_completo(' angelina', 'JOLIE'))
print(nome_completo('FELICITY     ', ' jones '))

--------------------------------------------------------------

# Em funções Python podemos ter nenhuma ou várias entradas, Em lambda também

def amar(): return 'Como não amar Python?'

def uma(x): return 3*x + 1

def duas(x, y): return (x*y)**0.5

def tres(x, y, z): return 3/(1/x+1/y+1/z)
# n = lambda x1, x2, ... xn: <expressão>

print(amar())
# Como não amar Python?

print(uma(6))
# 19

print(duas(5, 7))
# 5.916079783099616

print(tres(3, 6, 9))
# 4.909090909090908

# OBS: Se passarmos mais argumentos do que parâmetros esperados teremos TypeError

----------------------------------------------------------------

# Outro Exemplo

autores = ['Issac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke',
           'Frank Herbert', 'Orson Scott Card', 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']


# Ordenação por sobrenome
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)
# ['Douglas Adams', 'Issac Asimov', 'Leigh Brackett', 'Ray Bradbury', 'Orson Scott Card',
# 'Arthur C. Clarke', 'Robert Heinlein', 'Frank Herbert', 'H. G. Wells']

'''

# Função Quadrátrica
# f(x) = a*x**2 + b*x + c


def gerador_funcao_quadratica(a, b, c):
    """ Retorna a função f(x) = a*x**2 + b*x + c"""
    return lambda x: a*x**2 + b*x + c


teste = gerador_funcao_quadratica(2, 3, -5)

print(teste(0))
# -5

print(teste(1))
# 0

print(teste(2))
# 9

print(gerador_funcao_quadratica(3, 0, 1)(2))
# 13
