'''
# Generators (Geradores)

def nums(): 
    for num in range(1,10):
        yield num

ge1= nums()

print(ge1) # Generation Expression
# <generator object nums at 0x00000235FC4B60A0>

print(next(ge1))
# 1

print(next(ge1))
# 2 
'''

# Realizando o teste de velocidade
import time

# Generator Expression
gen_inicio = time.time()
print(sum(num for num in range(100000)))
gen_tempo = time.time() - gen_inicio

# List Comprehension
list_inicio = time.time()
print(sum(num for num in range(100000)))
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
# 0.005585432052612305

print(f'List Comprehension levou {list_tempo}')
# 0.004993438720703125
