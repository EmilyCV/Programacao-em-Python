def soma_lisa(lista): 
    return sum(lista)

if __name__ == '__main__':
    lista = [1,2,3,4,5,6,7,8,9,10]
    print(soma_lisa(lista))
    
    tupla = (1,2,3,4,5,6,7,8,9,10)
    print(soma_lisa(tupla))
else:
    print('O módulo func.py foi importado')