'''
POO - Atributos

Atributos -> Representam as características do objeto. Ou seja, pelos atributos nós conseguimos 
representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância;
    - Atributos de Classe;
    - Atributos Dinâmicos;
    
# Atributos de instância: São atributos declarados dentro do método construtor.

# OBS: Métodos construtor: É um método especial utilizado para a contrução do objeto. 

# Em Java, uma classe Lâmpada, incluindo seus atributos ficaria mais ou menos:

public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;
    
    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
}

Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é publico. Ou seja,
pode ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja, que
deve ser acessado/utilizado somente dentro da própria classe onde está declarado, utiliza-se __ duplo no início de seu nome.

Isso é conhecido também como Name Mangling.
'''


class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self._ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos Públicos e Atributos Privados
class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


''' # OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Pytho não vai impedir que façamos 
# acesso aos atributos sinalizados como privados fora da classe.

# Exemplo

user = Acesso('user@gmail.com', '123456')


print(user.email)
# user@gmail.com

# print(user.__senha) # AttributeError

print(dir(user))
# ['_Acesso__senha', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'email', 'mostra_email', 'mostra_senha'] 

print(user._Acesso__senha) # Temos acesso, mas não deveríamos fazer este acesso.
# 123456

user.mostra_senha()
# 123456

user.mostra_email()
# user@gmail.com

# O que significa atributos de instância?

# Significa, que ao criarmos instâncias/objetos de uma classe, todas as instâncias terão estes atributos.

user1 = Acesso('user1@gmail.com', '12345')
user2 = Acesso('user2@gmail.com', '54321')

user1.mostra_email()
# user1@gmail.com

user2.mostra_email()
# user2@gmail.com '''


# Atributos de Classe

# Atributos de classe, são atributos, claro, que são declarados diretamente na classe, ou seja, fora do construtor.
# Geralmente já  inicializamos um valor, e este valor é compartilhado entre todas as instâncias da classe. Ou seja,
# Ao invés de cada instância da classe ter seus próprios valores como é o caso dos atributos de instância, com os
# atributos de classe todas as instâncias terão o mesmo valor para este atributo.

class Produto:
    # atributo de classe
    imposto = 1.05  # 0.05 de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


'''# Atributos de Classe

p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

print(p1.valor) # Acesso possível, mas incorreto de um atributo de classe
print(p2.valor) # Acesso possível, mas incorreto de um atributo de classe

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto) # Acesso correto de um atributo de classe

print(p1.id)

print(p2.id)

# OBS: Em linguagens como Java, os atributos conhecidos como atributos de classe aqui em Python são 
# chamados de atributos estáticos; '''

# Atributos Dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução.

# OBS: O atributo dinâmico será exclusivo da instância que o criou.

p1 = Produto('PlayStation 4', 'Video Game', 2300)

p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg'  # Note que na classe Produto não existe o atributo peso

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')

# Deletando atributos

print(p1.__dict__)
# {'id': 1, 'nome': 'PlayStation 4', 'descricao': 'Video Game', 'valor': 2415.0}

print(p2.__dict__)
# {'id': 2, 'nome': 'Arroz', 'descricao': 'Mercearia', 'valor': 6.2895, 'peso': '5kg'}

print(Produto.__dict__)

del p2.peso
del p2.valor
del p2.descricao

print(p1.__dict__)
# {'id': 1, 'nome': 'PlayStation 4', 'descricao': 'Video Game', 'valor': 2415.0}

print(p2.__dict__)
# {'id': 2, 'nome': 'Arroz'}