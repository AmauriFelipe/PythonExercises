from time import sleep
from random import randint
jogcomp = randint(1,3)
print('+='*20)
print('\033[1;34mVou jogar pedra, papel e tesoura com você.\033[m')
print('+='*20)
print('Digite 1 para pedra, 2 para papel e 3 para tesoura e em seguida Enter.')
resposta1 = str(input('Vamos lá? (s/n): '))
print(' ')
if resposta1 == 'n':
    print('Ok.')
elif resposta1 == 's':
    print('Se prepare...')
    print(' ')
    sleep(1)
    print('1...')
    print(' ')
    sleep(1)
    print('2...')
    print(' ')
    sleep(1)
    print('3...')
    print(' ')
    sleep(1)
    print('\033[1;31mVAI!\033[m')
    resposta2 = int(input('Sua jogada: '))
    print(' ')
    if resposta2 == 1 and jogcomp == 1:
        print('Eu jogo \033[1;33mPEDRA\033[m! Você também jogou pedra, \033[1;33mEMPATAMOS\033[m.')
    elif resposta2 == 1 and jogcomp == 2:
        print('Eu jogo \033[1;31mPAPEL\033[m! Você jogou pedra, \033[1;31mEU GANHEI!\033[m Tadinho...')
    elif resposta2 == 1 and jogcomp == 3:
        print('Eu jogo \033[1;32mTESOURA\033[m! Você jogou pedra, \033[1;32mVOCÊ GANHOU!\033[m Foi pura sorte...')
    elif resposta2 == 2 and jogcomp == 1:
        print('Eu jogo \033[1;32mPEDRA\033[m! Você jogou papel, \033[1;32mVOCÊ GANHOR!\033[m Foi pura sorte...')
    elif resposta2 == 2 and jogcomp == 2:
        print('Eu jogo \033[1;33mPAPEL\033[m! Você jogou papel, \033[1;33mEMPATAMOS.\033[m')
    elif resposta2 == 2 and jogcomp == 3:
        print('Eu jogo \033[1;31mTESOURA\033[m! Você jogou papel, \033[1;31mEU GANHEI!\033[m Tadinho...')
    elif resposta2 == 3 and jogcomp == 1:
        print('Eu jogo \033[1;31mPEDRA\033[m! Você jogou tesoura, \033[1;31mEU GANHEI!\033[m Tadinho...')
    elif resposta2 == 3 and jogcomp == 2:
        print('Eu jogo \033[1;32mPAPEL\033[m! Você jogou tesoura, \033[1;32mVOCÊ GANHOU!\033[m Foi pura sorte...')
    elif resposta2 == 3 and jogcomp == 3:
        print('Eu jogo \033[1;33mTESOURA\033[m! Você jogou tesoura, \033[1;33mEMPATAMOS.\033[m')
    elif resposta2 != 1 and resposta2 != 2 and resposta2 != 3:
        print('Sua resposta não foi válida. Tá pensando que vai quebrar meu programa? vai sonhando!')
else:
    print('Sua resposta não foi válida. Tá pensando que vai quebrar meu programa? vai sonhando!')
