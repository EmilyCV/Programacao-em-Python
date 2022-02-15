'''
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode
realizar no seu sistema.

Em Python, dividimos os métodos, em 2 grupos: Métodos de instância e Métodos de Classe

# Método de Instância

# O método dunder init __init__ é um método especial chamado de construtor e  sua função
é construir o objeto a partir da classe.

OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.

Por mais que possamos criar nossas próprias funções utilizando dunder (__nomefuncao__) não é aconselhado.
Python possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o comportamento dessas funções mágicas
internas da linguagem. Então, evite ao máximo.

# Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palavras separadas por __

'''


class Lampada:
    def __index__(self, cor, voltagem, luminosidade, ligado):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligado = False


class ContaCorrente:
    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = numero
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        '''Retorna o valor do produto com o desconto'''
        return(self.__valor * (100 - porcentagem)) / 100

# p1 = Produto('PlayStation 4', 'Video Game', 2300)

# print(p1.desconto(20))

# print(Produto.desconto(p1, 40))

from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:
    
    contador = 0
    
    @classmethod
    def conta_usuario(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuários no sistema')
        
    @classmethod
    def ver(self):
        print('Teste')    
        
    @staticmethod
    def definicao():
        return 'UXR344'    
        
    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]

    


user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')
user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')


print(user1.nome_completo())
# Angelina Jolie

print(Usuario.nome_completo(user1))
# Angelina Jolie

print(user2.nome_completo())
# Felicity Jones

# Acesso de forma errada de um atributo de classe
print(f'Senha: {user1._Usuario__senha}')
# Senha: $pbkdf2-sha256$200000$854TohRCiFHK.f./1zonJA$LsjENAc16pyWmTaBjoTT8Xr5Wc8GSxXdd9Id.fuL91g

senha = input('Informe a senha: ')

if user1.checa_senha(senha):
    print('Acesso permitido.')
else:
    print('Acesso negado.')
    
print(f'Senha User Criptografada: {user1._Usuario__senha}') # Acesso errado

Usuario.conta_usuario() # Forma correta
user1.conta_usuario() 

print(user1._Usuario__gera_usuario()) # Acesso de forma ruim
# angelina

# Método Estático

print(Usuario.contador)
# 2

print(Usuario.definicao())
# UXR344

print(user1.contador)
# 2

print(user1.definicao())
# UXR344