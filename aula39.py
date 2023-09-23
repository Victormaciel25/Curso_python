"""
Iterando strings com while
"""

nome = 'Victor de Oliveira Maciel Rodrigues' #Iteráveis

tamanho_nome = len(nome)
contador = 0
novo_nome = ''

while contador < len(nome):
    letra = nome[contador]
    novo_nome += letra
    contador = contador + 1

print(novo_nome)