'''
O *args é um parâmetro, como outro qualquer. Isso significa que você poderá chamar de qualquer 
coisa desde que comece com asterisco. Ex: *xis

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla(imutáveis).


----------------------------------------------------------------

# args não é obrigatório


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(1, 2))
print(soma_todos_numeros(1, 2, 3))
print(soma_todos_numeros(1, 2, 3, 4))


'''


def soma_todos_numeros(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Desempacotar
print(soma_todos_numeros(*numeros))

'''OBS: O asterisco serve para que informemos ao Python que estamos passando como argumento uma coleção
de dados. Desta forma, ele saberá que precisará desempacotar estes dados.'''
