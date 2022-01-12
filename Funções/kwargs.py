'''
**kwargs -> Poderiamos chamar este parâmetro de **zix, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extas em uma tupla, 
o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário.

----------------------------------------------------------------

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}.')


cores_favoritas(marcos='verde', julia='amarelo',
                fernanda='azul', vanessa='branco')

# OBS: os parâmetros *args e **kwargs não são obrigatórios.

cores_favoritas()
cores_favoritas(geek='roxo')

----------------------------------------------------------------

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return "Não tenho certeza quem você é..."

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial')) 

----------------------------------------------------------------

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

----------------------------------------------------------------

# Entenda por quê é importante manter a ordem dos parâmetros na declaração


def mostra_info(a, b, *args, intrutor='Geek', **kwargs):
    return[a, b, args, intrutor, kwargs]


"""
a = 1
b = 2
args = (3,)
instrutor = 'Geek'
kwargs = {'sobrenome': 'University', 'cargo':'Instrutor'}
"""

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))
#[1, 2, (3,), 'Geek', {'sobrenome': 'University', 'cargo': 'Instrutor'}]

----------------------------------------------------------------

#Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))

'''


def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a+b+c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
# 6
soma_multiplos_numeros(*tupla)
# 6
soma_multiplos_numeros(*conjunto)
# 6

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)
# 6

# OBS: Os nomes da chave em um dicionário devem ser o mesmo dos parâmetrosda função

soma_multiplos_numeros(*dicionario, nome='Geek')
# abc

soma_multiplos_numeros(**dicionario, lang='Python')
