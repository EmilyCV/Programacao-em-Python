'''
Métodos Mágicos, são todos os métodos que utilizam dunder.

dunder init -> __init__()

Dunder -> Double Underscore

dunder repr -> Representação do objeto
'''


class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return self.titulo

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Um objeto do tipo Livro foi deletado da memória')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += '' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geeek University', 350)

print(str(livro1))
# Python Rocks!

print(livro2)
# Inteligência Artificial com Python

print(len(livro1))
# 400

print(len(livro2))
# 350

print(livro1 + livro2)
# Python Rocks! - Inteligência Artificial com Python

print(livro1*3)
# Python Rocks!Python Rocks!Python Rocks!
