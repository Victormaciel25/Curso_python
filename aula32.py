"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou impar. Caso o usuário não digite um número inteiro, informe que não é um número
inteiro.
"""

try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Isso não é um número inteiro.")

if numero % 2 == 0:
    print('O numero é par.')
elif numero % 2 != 0:
    print('O numero é impar.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex.: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = int(input('Que horas são? '))

if horario >= 0 and horario <= 11:
    print('Bom dia')
elif horario >= 12 and horario <=17:
    print('Boa tarde')
elif horario >= 18 and horario <= 23:
    print('Boa noite')
else:
    print('Não conheço essa hora')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Qual o seu nome? ')
numero_letras = len(nome)

if numero_letras <= 4:
    print('Seu nome é curto')
elif numero_letras == 5 or numero_letras == 6:
    print('Seu nome é normal')
elif numero_letras > 6:
    print('Seu nome é muito grande')
