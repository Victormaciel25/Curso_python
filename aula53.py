"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = list(enumerate(lista))
# for indice, nome in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

print(lista_enumerada)

