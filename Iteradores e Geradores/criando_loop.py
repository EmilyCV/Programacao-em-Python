def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break
    
meu_for('Geek University')

numeros = [1, 2, 3, 4, 5, 6]

meu_for(numeros)