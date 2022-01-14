'''
Set Comprehension

Lista = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}
'''

# Exemplos

numeros = {num for num in range(1, 7)}

print(numeros)
# {1, 2, 3, 4, 5, 6}

# Exemplo

numeros = {x**2 for x in range(10)}

print(numeros)
# {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}


numeros = {x: x**2 for x in range(10)}

print(numeros)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

#Exemplo

letras = {letra for letra in 'Geek University'}

print(letras)
# {' ', 'G', 'i', 't', 'k', 'r', 'v', 'y', 'U', 'e', 's', 'n'}
