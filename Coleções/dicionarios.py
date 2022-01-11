"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionais são coleçoes do tipo chave/valor

Dicionários são representados por chaves

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos "chave":"valor";
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;
    
-----------------------------------------------------------------------------
    
#Crição de dicionários

#Forma 1 (Mais comum)
paises = {"br" : "Brasil", "eua":"Estados Unidos", "py":"Paraguia"}

print(paises)
print(type(paises))

#Forma 2 (Menos comum)
paises = dict(br = "Brasil", eua="Estados Unidos", py = "Paraguia")

print(paises)
print(type(paises))

-----------------------------------------------------------------------------

paises = {"br" : "Brasil", "eua":"Estados Unidos", "py":"Paraguia"}

#Acessando elementos

#Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises["br"])
print(paises["py"])
# print(paises["ru"])
#Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

#Forma 2 - Acessando via get - Recomendada

print(paises.get("br"))
print(paises.get("ru"))

-----------------------------------------------------------------------------

paises = {"br" : "Brasil", "eua":"Estados Unidos", "py":"Paraguia"}

pais = paises.get("ru", "Não Encontrado")  #Pegue o valor ru, caso não encontre print "Não Encontrado"

print(pais)

-----------------------------------------------------------------------------
paises = {"br" : "Brasil", "eua":"Estados Unidos", "py":"Paraguia"}

#Podemos verificar se determinada chave se encontra em um dicionário
print( 'br' in paises )
print( 'ru' in paises )
print( 'Estados Unidos' in paises )

if "ru" in paises:
    russia = paises["ru"]

-----------------------------------------------------------------------------

#Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, tupla dicionário, 
#como chaves de dicionários

#Tuplas são interessantes serem usadas como chaves de dicionários pois as mesmas são imutáveis
localidades = {
    (35.6895, 39.6917): "Escritório em Tókio",
    (40,7128, 74.0060): "Escritório em Nova York",
    (37.7749, 122.4194): "Escritório em São Paulo",
}

print(localidades)
print(type(localidades))

-----------------------------------------------------------------------------

#Adicionar elementos em um dicionário
receita = { "jan":100, "fev": 120, "mar":300}

print(receita)
print(type(receita))

#Forma 1
receita["abr"] = 350
print(receita)

#Forma 2

novo_dado = {"mai":500}

receita.update(novo_dado) #receita.update({"mai":500})

print(receita)

#Atualizando dados em um dicionário

#Forma 1

receita["mai"]= 550

print(receita)

#Forma 2

receita.update({"mai":600})

print(receita)

#CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
#CONCLUSÃO 2: Em dicionários não podemos ter chaves repetidas.

-----------------------------------------------------------------------------

#Remover dados de um dicionário
receita = { "jan":100, "fev": 120, "mar":300}

#Forma 1 - Mias Comum
ret = receita.pop("mar")
print(ret)
print(receita)

#OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado
#OBS 2: Ao removermos um objeto, o valor deste objeto sempre é retornado.

#Forma 2

del receita["fev"]

print(receita)

#Se a chave não existir será gerado um KeyError
#OBS: Neste caso o valor removido não é retornado

-----------------------------------------------------------------------------

#Metodo de dicionários

d = dict(a=1,b=2,c=3)

print(d)
print(type(d))

#Limpar o dicionário (Zerar dados)

d.clear()
print(d)

#Copiando um dicionário para outro

#Forma 1 #Deep Copy

novo = d.copy()
print(novo)

novo["d"] = 4
print(d)
print(novo)

#Forma 2  #Shallow Copy

novo = d

print(d)

novo["d"] = 4

print(d)
print(type(d))
"""

#Forma não usual de criação de dicionários

outro = {}.fromkeys("a", "b")

print(outro)
print(type(outro))

usuario = {}.fromkeys(["nome", "pontos", "email", "profile"], "desconhecido")

print(usuario)
print(type(usuario))

#O método fromkeys recebe dois parâmetros: um iterável e um valor.
#Ele vai gerar para cada valor do iterável uma chave e irá atribuir a está chave o valor informado

veja = {}.fromkeys("teste", "valor")
print(veja)

veja = {}.fromkeys(range(1,11), "novo")
print(veja)