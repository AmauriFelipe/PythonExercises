print('Esse programa vai analisar se você poderá adquirir um empréstimo.')
print(' ')
casa = float(input('Digite o valor da casa: R$'))
salário = float(input('Digite o seu salário: R$'))
anos = int(input('Digite em quantos anos você irá pagar: '))
prestação = casa/(anos*12)
print(' ')
print('Para pagar uma casa de R${:.2f} em {:.2f} anos,'.format(casa,anos))
print('a prestação será de R${:.2f}.'.format(prestação))
print(' ')
if prestação <= salário*0.3:
    print('\033[1;32mO seu empréstimo foi aceito.\033[m')
else:
    print('\033[1;31mO seu empréstimo foi negado.\033[m')