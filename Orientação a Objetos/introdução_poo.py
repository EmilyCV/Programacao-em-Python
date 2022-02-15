'''
Programação Orientada a Objetos - POO

- POO é um paradigma de programação que utiliza mapeamento de objetos do mundo real para que 
modelos computacionais.

- Paradigma de programação é a forma/metodologia utilizada para pensar/desenvolver sistemas.

Principais elementos da Orientação a Objetos:
    - Classe -> Modelo do objeto do mundo real sendo representado computacionalmento;
    - Atributo -> Características do objeto;
    - Método -> Comportamento do objeto (funções);
    - Construtor -> Método especial utilizado para criar os objetos;
    - Objeto -> Instância da classe;
'''

numero = 10

print(numero)
# 10
print(type(numero))
# <class 'int'>

nome = 'Geek'

print(nome)
# Geek
print(type(nome))
# <class 'str'>

class Produto:
    pass

ps4 = Produto()
print(ps4)
# <__main__.Produto object at 0x000001BF2C997D60>
print(type(ps4))
# <class '__main__.Produto'>