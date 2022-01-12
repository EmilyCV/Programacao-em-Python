import random

a = random.sample(range(100), 10)
b = random.sample(range(100), 10)
c = []

print('Lista A:', a)
print('Lista B:', b)

for i in range(len(a)):
    c.append(a[i])
    c.append(b[i])

print('Lista C:', c)