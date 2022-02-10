'''
Decorators com diferentes assinaturas

----------------------------------------------------------------

# Relembrando

def gritar(funcao): 
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'

def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


# Teste
print(saudacao('Angelina'))
# OLÁ, EU SOU O/A ANGELINA

print(ordenar('Picanha', 'Batata Frita'))
# Olá, eu gostaria de Picanha, acompanhado de Batata Frita, por favor.


# Para resolver, utilizamos um padrão de projeto chamado Decorator Pattern

A assinatura de uma função é  represenntada pelo seu retorno, nome e parâmetros de entrada.

----------------------------------------------------------------

# Refatorando com a Decorator Pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'

print(saudacao('Angelina'))

print(ordenar('Picanha', 'Batata Frita'))

@gritar
def lol():
    return 'lol'

print(lol())

# OBS: Vale lembrar que podemos utilizar parâmetros nomeados

print(ordenar(acompanhamento='Batata Frita', principal = 'Picanha'))
'''

# Decorator com argumentos

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)
    
@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

# Testando
print(soma_dez(10,12))
# 22

print(soma_dez(1,21))
# Valor incorreto! Primeiro argumento precisa ser 10

print(comida_favorita('pizza', 'churrasco'))
# ('pizza', 'churrasco')

print(comida_favorita('sanduiche', 'churrasco'))
# None
# Valor incorreto! Primeiro argumento precisa ser pizza