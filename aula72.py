# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

import os

def mult(*args):
    total = 1
    for numero in args:
        total *= int(numero)
    return total

print('Selecione uma opção')
opcao = input('[i]nserir [P]arar')

total = 1

while True:
    if opcao == 'i':
        os.system('cls')
        total = mult(input('Valor: '), total)
        opcao = input('[i]nserir [P]arar')
    elif opcao == 'p':
        print(total)
        print('Você encerrou a multiplicação.')
        break
    else:
        print('Selecione [i]nserir ou [P]arar')
    
if total % 2 == 0:
    print('O numero é par')
else:
    print('O numero é impar')
