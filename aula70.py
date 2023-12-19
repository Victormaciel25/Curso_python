"""
Retorno de valores das funções (return)
"""

def soma(x, y):
    print('Olha')
    print('só que')
    print('legal')
    return x + y
    print(1+1) # o 'return' irá executar o que foi mandado e finalizará a execução, ou seja, o 'print(1+1)' não será executado.

#variavel = soma(1, 2)
#variavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1 + soma2)

def soma(x, y):
    if x > 10:
        return (10, 20)
    return x + y

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))
