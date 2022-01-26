'''
Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo assim que o
programa para de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é: 
try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema
    
--------------------------------------------------------------

# Exemplo 1 - Tratando um erro genérico

try:
    len(5)
except:
    print('Deu algum problema')
    
# OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE tratar de forma específica.

--------------------------------------------------------------

# Exemplo 2 - Tratando um erro específico

try: 
    len(5)
except TypeError as e:
    print(f'A aplicação gerou o seguinte erro: {e}')
    # A aplicação gerou o seguinte erro: object of type 'int' has no len()
    
--------------------------------------------------------------

try: 
    # len(5)
    geek()
except NameError as e:
    print(f'Deu NameError: {e}')
    # Deu NameError: name 'geek' is not defined
except TypeError as e:
    print(f'Deu TypeError: {e}')
    # Deu TypeError: object of type 'int' has no len()

'''


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {'nome': 'geek'}
print(pega_valor(dic, 8))
