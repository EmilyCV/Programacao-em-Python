# Soma de elementos abaixo da diagonal principal

from func_ex_48_49_50_51 import func_matriz, mostrar_matriz

matriz = func_matriz()
print(mostrar_matriz())

# print(matriz)

soma = 0
for x in range(len(matriz)):
    for y in range(len(matriz)):
        if x > y:
            soma = soma + matriz[x][y]

print('Soma de elementos abaixo da diagonal principal:', soma)
