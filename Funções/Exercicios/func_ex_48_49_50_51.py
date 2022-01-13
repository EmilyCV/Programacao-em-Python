def func_matriz(l=3, c=3):
    matriz = [[7, 8, 9], [5, 8, 0], [6, 5, 9]]
    # for i in range(l):
    #     linha = random.sample(range(10), l)
    #     matriz.append(linha)
    return matriz

def mostrar_matriz(l=3, c=3):
    matriz = func_matriz()
    # Forma de printar a matriz
    for i in range(l):
        for j in range(c):
            print("{:<3}".format(matriz[i][j]), end=' ')
        print()
        
# print(func_matriz())
# print(mostrar_matriz())