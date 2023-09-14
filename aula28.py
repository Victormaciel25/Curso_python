"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exibar:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

nome = (input('Digite seu nome: '))
idade = (input('Digite sua idade: '))
def tem_espaços(nome):
    if ' ' in nome:
        return True
    else:
        return False
    
if not nome or not idade:
    print("Desculpe, você deixou campos vazios.")
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if tem_espaços(nome):
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print('Seu nome tem ',len(nome),' letras.')
    print('A primeira letra do seu nome é ',(nome[0]))
    print('A ultima letra do seu nome é ',(nome[-1]))





