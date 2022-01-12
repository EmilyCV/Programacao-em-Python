import random

a = random.sample(range(100), 6)
print('Lista aleátoria A:', a)

# a)

b = a.copy() + [1, 0, 5, -2, -5, 7]
print('Lista B:', b)

# b)

c = [a[0], a[1], a[5]]
print('Soma:', sum(c))

# c)
a[3] = 100

print(a)

# d)
for i in range(len(a)):
    print(a[i])