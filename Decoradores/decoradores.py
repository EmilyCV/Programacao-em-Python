'''
- Decorators são funções;
- Decorators envolvem outras funções e aprimoram sues comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando '@' (Syntact Sugar / Açúcar Sintático)

|------------------------------------------|
|           Function Decorator             |
|------------------------------------------|

|----------------------------------------------|
| |------------------------------------------| |
| |             Função Decorada              | |
| |------------------------------------------| |
|----------------------------------------------|

----------------------------------------------------------------
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo

def saudacao():
    print('Seja bem-vindo(a) à Geek University')
    
# Teste 1

teste = seja_educado(saudacao)

teste()
# Foi um prazer conhecer você!
# Seja bem-vindo(a) à Geek University
# Tenha um ótimo dia!

# Teste 2
def raiva():
    print('Eu te odeio!')

raiva_educada = seja_educado(raiva)

raiva_educada()
# Foi um prazer conhecer você!
# Eu te odeio!
# Tenha um ótimo dia!

'''
# Decorators com Syntax Sugar

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')
    
# Teste

apresentando()
# Foi um prazer conhecer você!
# Meu nome é Pedro
# Tenha um ótimo dia!

@seja_educado_mesmo
def dormir():
    print('Quero dormir')
    
dormir()
# Foi um prazer conhecer você!
# Quero dormir
# Tenha um ótimo dia!