# Soma da diagonal secundaria

from func_ex_48_49_50_51 import func_matriz, mostrar_matriz

matriz = func_matriz()

print(mostrar_matriz())

soma = 0
z = - 1
for x in range(len(matriz)):
    soma = soma + matriz[x][z]
    z = z - 1

print('Soma dos elementos da diagonal secundária:', soma)
