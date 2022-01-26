'''
raise -> Lança exceções

OBS: O raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra do Python.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens de erro.

A forma geral de utilização é:

raise  TipodoErro("Mensagem de erro")

----------------------------------------------------------------

# Exemplo


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError("texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("cor precisa ser uma string")
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek', 'azul')
# O texto Geek será impresso na cor azul

colore('Geek', 1)
# TypeError: cor precisa ser uma string

colore(True,  'azul')
# TypeError: cor precisa ser uma string

'''


def colore(texto, cor):
    cores = ('verde', 'azul', 'amarelo', 'branco')
    if type(texto) is not str:
        raise TypeError("texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("cor precisa ser uma string")
    if cor not in cores:
        raise TypeError(f"cor precisa ser uma entre: {cores}")
    print(f'O texto {texto} será impresso na cor {cor}')
    
colore('Geek',  'roxo')
# TypeError: cor precisa ser uma entre: ('verde', 'azul', 'amarelo', 'branco')

colore('Geek',  'azul')
# O texto Geek será impresso na cor azul

# OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado.