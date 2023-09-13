"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a quantidade de caracteres da string.
"""

variavel = 'Olá mundo'
print(variavel[4:8])
print(len(variavel))
print(variavel[0:9:2]) # O 2 é a quantidade de letras que ele pula.
print(variavel[-1:-10:-1]) # Negativo a variável fica invertida.