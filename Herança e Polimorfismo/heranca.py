''' 
A ideia de herança é a de reaproveitar código. Também extender nossas classes.

OBS: com a herança, a partir de uma classe existente, nós extendemos outra classe que passa a herdar atributos
e métodos da classe herdada.

OBS: Quando uma classe herda de outra classe ela herda TODOS os atributos e métodos da classe  herdada.

'''


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf) # Forma não comum de acessas dados da super classe
        self.__renda = renda


class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf) # Forma comum de acessas dados da super classe
        self.__matricula = matricula

        # Sobrescrita de método
        def nome_completo(self):
            print(super().nome_completo())
            print(self._Pessoa__cpf)
            return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'


class Pinguim:
    def __init__(self, nome, sobrenome):
        self.__nome = nome
        self.__sobrenome = sobrenome


client1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-00', 1234)

print(client1.nome_completo())
print(funcionario1.nome_completo())

print(client1.__dict__)
print(funcionario1.__dict__)
