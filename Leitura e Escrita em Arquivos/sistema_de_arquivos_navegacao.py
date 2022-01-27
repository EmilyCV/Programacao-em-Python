'''
Sistema de Arquivos e Navegação

Para fazer uso da manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo os.

os - > Operating System - Sistema Operacional

--------------------------------------------------------------

import os

# getcwd() - > pega o current work directory - diretório de trabalho corrente

print(os.getcwd())
# C:\Work\Curso\Python

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd())
# C:\Work\Curso

----------------------------------------------------------------

import os 

# Podemos checar se um diretório é absoluto ou relativo

print(os.path.isabs('/Curso/Python/'))
# True

----------------------------------------------------------------

import os, platform

# Podemos identificar o sistema operacional com o módulo os
print(os.name) # psix (Linux e Mac), nt (Windowns)

# Podemos ter mais detalhes no sistema operacional
# print(os.uname()) # Linux

print(platform.uname()) # Windows

print(platform.uname()[0]) 
# Windows

----------------------------------------------------------------

import os

print(os.getcwd())

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o
# diretório que será juntado ao atual.
os.path.join(os.getcwd(), 'Geek')

print(os.getcwd())

'''

import os

scanner = os.scandir()

# Podemos listar os arquivos e diretórios com o listdir()
print(os.listdir())

# Podemos listar os arquivos e diretórios com mais detalhes com o scandir()
arquivos = list(os.scandir())

print(arquivos)

print(dir(arquivos[0]))

print(arquivos[0].inode()) # ??
print(arquivos[0].is_dir()) # É um diretório?
print(arquivos[0].is_file()) # É um arquivo?
print(arquivos[0].is_symlink()) # É um link simbólico?
print(arquivos[0].name) # Nome do arquivo
print(arquivos[0].path) # Caminho até o arquivo
print(arquivos[0].stat()) # Estatísticas

# OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, assim quando abrimos um arquivo.

scanner.close()