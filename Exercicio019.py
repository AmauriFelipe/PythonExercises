from random import choice
a1 = str(input('Escreva o nome do 1º aluno: '))
a2 = str(input('Escreva o nome do 2º aluno: '))
a3 = str(input('Escreva o nome do 3º aluno: '))
a4 = str(input('Escreva o nome do 4º aluno: '))
s = [a1, a2, a3, a4]
n = choice(s)
print('A nova ordem de nomes é {}.'.format(n))