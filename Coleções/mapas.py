"""
Mapas -> Dicionários
Dicionários -> {}

----------------------------------------------------------------
receitas = {"jan": 100, "fev" : 250, "mar" : 400}

#Interar sobre dicionários
for chave in receitas:
    print(chave)

for chave in receitas:
    print(receitas[chave])

for chave in receitas:
    print(f"{chave} : {receitas[chave]}")
    
----------------------------------------------------------------
receitas = {"jan": 100, "fev" : 250, "mar" : 400}

print(receitas)


print(receitas.keys())

for chave in receitas.keys():
    print(receitas[chave])


"""

receitas = {"jan": 100, "fev" : 250, "mar" : 400}

print(receitas)

#Acessando os valores

print(receitas.values())

for valor in receitas.values():
    print(valor)
    
#Desempacotamento de dicionários

for chave, valor in receitas.items():
    print(f"Chave = {chave} \nValor = {valor}")

#Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
#*Se os valores forem todos inteiros ou reais

print(sum(receitas.values()))
print(max(receitas.values()))
print(min(receitas.values()))
print(len(receitas))