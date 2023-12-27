# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
       'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25', 
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5', 
    },
]
cont = 0
for pergunta in perguntas:
    print(('Pergunta: ') + pergunta['Pergunta'])
    contador = 1
    print('Opção:')
    for opcao in pergunta['Opções']:
        print(str(contador) + ')' + opcao)
        contador += 1       
    resp = input('Escolha uma opção: ')
    if resp == pergunta['Resposta']:
        print('Acertou')
        cont += 1
    else:
        print('Errou')

print('Você acertou ' + str(cont) + ' de 3 perguntas.')