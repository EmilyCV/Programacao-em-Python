'''
Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será
criada e o valor default será atribuido.

OBS: Lambdas são funções sem nome, que ppodem ou não receber parâmetros de entrada e retorna valores

'''

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)
# defaultdict(<function <lambda> at 0x00000285198BA710>, {'curso': 'Programação em Python: Essencial'})

print(dicionario['outro'])  # 0

print(dicionario)
# defaultdict(<function <lambda> at 0x000001509468A710>, {'curso': 'Programação em Python: Essencial', 'outro': 0})
