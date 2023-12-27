# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.

# Criando um set
# Set(iterável) ou {1, 2, 3}

# s1 = set('Luiz')
s1 = set() # vazio
s1 = {'Luiz', 1, 2, 3} # com dados
print(s1)

# Sets são eficientes para remover valores duplicados de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - Não tem índexes;
# - Não garantem ordem;
# - São iteráveis (for, in, not in)
l1 = {1, 2, 3, 3, 3, 3, 3, 1}
s1 = set(l1)
l2 = list(s1)
s1 = {1, 2, 3}
print(3 not in s1)
for numero in s1:
    print(numero)


# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# União | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# 