import random

x = tuple(random.sample(range(100), 5))
y = tuple(random.sample(range(100), 5))
z = []

for i in range(len(x)):
    z.append(x[i]*y[i])
    
print('Lista X:', x)
print('Lista Y:', y)

# x1*y1+x2*y2+x3*y3+x4*y4...xn*yn
print('Produto Escalar: ', sum(z))