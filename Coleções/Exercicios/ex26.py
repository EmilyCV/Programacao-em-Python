'''
Desvio Padrão = √(n∑i=1(v[i]-m)^2)/(n-1)
∑: símbolo de somatório. Indica que temos que somar todos os termos, desde a primeira posição (i=1) até a posição n
v[i]: valor na posição i no conjunto de dados
m: média aritmética dos dados
n: quantidade de dados
'''

a = [1,2,3,4,5,6,7,8,9,10]
m = sum(a)/len(a)

# Nova lista para fazer o calculo da somátoria
z = []

for i in range(len(a)):
    z.append((a[i]-m)**2)

dp = (sum(z)/(len(a)-1))**(1/2)

print("N:", len(a))
print("M", m)
print("Somatória:", sum(z))
print("O Desvio Padrão é:", dp)