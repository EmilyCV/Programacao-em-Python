'''
Documentando funções com Docstring

OBS: Podemos ter acesso á documentação de uma função em Python utilizando a propriedade especial __doc__

Podemos ainda fazer acesso á documentação com a funçao help()
'''


def diz_oi():
    """Uma função simples que retorna uma string 'Oi!'"""
    return 'Oi!'

# No terminal colocar from docstring import diz_oi e em seguida diz_oi.__doc__
