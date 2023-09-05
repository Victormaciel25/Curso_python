nome = 'Victor Maciel'
altura = 1.82
peso = 108
imc = peso / altura ** 2 

# Victor Maciel tem 1.82 de altura, pesa 108 quilos e seu IMC é 32,62.

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}.'

print(linha_1,linha_2,linha_3)