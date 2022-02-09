'''
Geradores (Generators) são Iterators (Iteradores):

OBS: O contrário não é verdadeiro. Ou  seja, nem todo itertor é um generator.

Outras informações: 
    - Generators podem ser criados com funções geradores.
    - Funções geradoras utilizam a palavra reservada yield
    - Generators podem ser criados com Expressões Geradoras.
    
Difereças entre Funçõe s e Generator Functions

-----------------------------------------------------------------------------------------
/ Funções                               / Generator Functions                           /      
-----------------------------------------------------------------------------------------
/ utilizam return                       / utilizam yeild                                /
-----------------------------------------------------------------------------------------
/ retorna uma vez                       / podem utilizar yield multiplas vezes          /
-----------------------------------------------------------------------------------------
/ quando executada, retorna um valor    / quanto executada, retorna um generator        /
-----------------------------------------------------------------------------------------
'''

# Exemplo Generator Function


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: Uma Generator Function não é um Generator. Ela gera um generator


gen = conta_ate(5)

print(type(gen))
# <class 'generator'>

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


gen = conta_ate(10)
print(next(gen))

for num in gen:
    print(num)


gen = list(conta_ate(10))
print(gen)
