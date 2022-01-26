'''
Utilizamos o gerenciados de pacotes Python chamado pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.org

colorama -> É utilizado para permitir impressão de textos com cor no terminal.

----------------------------------------------------------------

from colorama import init, Fore

init()

print(Fore.MAGENTA + 'Geek University')
print(Fore.BLUE + 'Geek University')
'''
# pip install python-pdf
import pydf

pdf = pydf.generate_pdf('<h1> Geek University </h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
