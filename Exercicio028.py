from random import randint
from time import sleep
print('Esse é o jogo da adivinhação. Estou pensando em um número inteiro entre 0 e 5.')
print(' ')
nr = randint(1, 5)
n = int(input('Em que número pensei? '))
print(' ')
print('Processando...')
print(' ')
sleep(2)
if n==nr:
    print('Você acertou!')
else:
    print('Você errou. Eu pensei no número {}, e não no {}'.format(nr, n))