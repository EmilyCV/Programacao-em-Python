'''
Deque -> É uma lista de alta performance
'''
from collections import deque

deq = deque('geek')
#deque(['g', 'e', 'e', 'k'])

print(deq)

# Adicionando elementos no deque

deq.append('y')

print(deq)
# deque(['g', 'e', 'e', 'k', 'y'])

# Adiciona no começo
deq.appendleft('k')

print(deq)
#deque(['k', 'g', 'e', 'e', 'k', 'y'])

print(deq.pop())
# y

print(deq)
#deque(['k', 'g', 'e', 'e', 'k'])
