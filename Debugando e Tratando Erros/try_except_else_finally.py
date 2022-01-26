'''
OBS:  A função do usuário é DESTRUIR seu sistema.

Else -> É executado somente se não ocorrer o erro.

--------------------------------------------------------------
# Else

num = 0

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor')
else:
    print(f'Você digitou {num}')
    
--------------------------------------------------------------

# Finally
try:
    num = int(input('Informe um número: '))
except ValueError:
    print(f'Você digitou um valor inválido.')
else: 
    print(f'Você digitou o número {num}')
finally:
    print("Executando o finally")
    
# OBS: O bloco finally é SEMPRE executado. Independente se houve exceção ou não.

# O finally, geralmente, é utilizado para fechar ou desalocar recursos.

----------------------------------------------------------------

def dividir(a, b):
    return a/b

num1 = int(input('Informe o primeiro número: '))

try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser númerico')
try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

----------------------------------------------------------------

# OBS: Você é responsável pelas entradas das suas funções. Então, trata-as!

def dividir(a, b):
    try:
        return a/b
    except ValueError:
        print('Valor incorreto')
    except ZeroDivisionError:
        print('Não é possível realizar uma divisão por zero')


num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

print(dividir(num1, num2))

'''

def dividir(a, b):
    try:
        return int(a)/int(b)
    except (ValueError,ZeroDivisionError) as e:
        return 'Ocorreu um problema: ',e
    
num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))