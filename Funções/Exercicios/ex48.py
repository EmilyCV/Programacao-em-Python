# Soma de elementos acima da diagonal principal

import random
from func_ex_48_49_50_51 import func_matriz, mostrar_matriz

matriz = func_matriz()

print(mostrar_matriz())

soma = 0
for x in range(len(matriz)):
    for y in range(len(matriz)):
        if y > x:
            soma = soma + matriz[x][y]

print('Soma de elementos acima da diagonal principal:', soma)
