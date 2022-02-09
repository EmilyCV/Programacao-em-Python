# Função usando listas 449MB

def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a+b
    return nums


# Teste
for n in fib_lista(10):
    print(n)

# Função usando geradores 3MB
def fib_lista(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a+b
        yield a
        contador += 1


# Teste
for n in fib_lista(10):
    print(n)
