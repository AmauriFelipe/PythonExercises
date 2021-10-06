#Programa que lê uma frase pelo teclado e mostre: 1-Quantas vezes aparece a letra A
#2-Em que posição aparece pela primeira vez
#3-Em que posição aparece pela última vez
frase = str(input('Escreva uma frase: ')).lower().strip()
print('A letra "A" aparece {} vezes nessa frase.'.format(frase.count('a')))
print('A primeira letra "A" aparece na posição {}'.format(frase.find('a')+1))
print('A última letra "A" aparece na posição {}'.format(frase.rfind('a')+1))