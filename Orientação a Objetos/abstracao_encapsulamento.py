'''
O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

Encapsular -> cápsula


.....................................
|                                   |
|       Atributos e métodos         |
|___________________________________|

# Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo um atributo privado chamado __nome e um método privado
chamado __falar()

Esses elementos privados só devem/deveriam ser acessados dentro da classe, mas Python não bloqueia este acesso
fora da classe. Com Python acontece um fenômeno chamado Name Mangling, que faz uma alteração na forma de se 
acessar os elementos privados, conforme:

_Classe__Elemento

Exemplo:

instancia._Pessoa__nome

instancia._Pessoa_falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privados do usuário.
'''


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(
            f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor deve ser positivo')

    def transferir(self, valor, conta_destino):
        # 1 - Remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10  # Taxa de tranferência para por quem realizou a tranferência

        # 2 - Adicionar o valor na sua conta de destino
        conta_destino.__saldo += valor


# conta1 = Conta('Geek', 150.00, 1500)

# # print(conta1.numero)
# # print(conta1.titular)
# # print(conta1.saldo)
# # print(conta1.limite)

# conta1.numero = 42
# conta1.titular = 'Xuxa'
# conta1.saldo = 9999999999999999
# conta1.limite = 99999999999999999999999

# print(conta1.__dict__)
# # {'_Conta__numero': 400, '_Conta__titular': 'Geek', '_Conta__saldo': 150.0, '_Conta__limite': 1500, 'numero': 42, 'titular': 'Xuxa', 'saldo': 9999999999999999, 'limite': 99999999999999999999999}

# conta1.extrato()
# # Saldo de 150.0 do titular Geek com limite de 1500

# print(conta1._Conta__titular)
# # Geek

# conta1._Conta__titular = 'Angelina'

# print(conta1.__dict__)
# # {'_Conta__numero': 400, '_Conta__titular': 'Angelina', '_Conta__saldo': 150.0, '_Conta__limite': 1500, 'numero': 42, 'titular': 'Xuxa', 'saldo': 9999999999999999, 'limite': 99999999999999999999999}

# conta1.depositar(150)

# print(conta1.__dict__)
# # {'_Conta__numero': 400, '_Conta__titular': 'Angelina', '_Conta__saldo': 300.0, '_Conta__limite': 1500, 'numero': 42, 'titular': 'Xuxa', 'saldo': 9999999999999999, 'limite': 99999999999999999999999}

# conta1.sacar(200)

# print(conta1.__dict__)
# # {'_Conta__numero': 400, '_Conta__titular': 'Angelina', '_Conta__saldo': 100.0, '_Conta__limite': 1500, 'numero': 42, 'titular': 'Xuxa', 'saldo': 9999999999999999, 'limite': 99999999999999999999999}

conta1 = Conta('Angelina', 150.00, 1500)
conta1.extrato()
# Saldo de 150.0 do titular Angelina com limite de 1500

conta2 = Conta('Felicity', 300, 2000)
conta2.extrato()
# Saldo de 300 do titular Felicity com limite de 2000

valor = 100

conta2.sacar(valor)

conta1.depositar(valor)

conta1.extrato()
# Saldo de 250.0 do titular Angelina com limite de 1500

conta2.extrato()
# Saldo de 200 do titular Felicity com limite de 2000

conta2.transferir(100, conta1)

conta1.extrato()
# Saldo de 350.0 do titular Angelina com limite de 1500

conta2.extrato()
# Saldo de 90 do titular Felicity com limite de 2000
