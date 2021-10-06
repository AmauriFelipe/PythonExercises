from time import sleep
print('''Soma de todos os números ímpares que são múltiplos
de 3 entre 1 e 500: ''')
sleep(1)
print(' ')
print('Calculando...')
print(' ')
sleep(1)
s = 0
cont = 0
for n in range(1, 500, 2):
    if n % 3 == 0:
        cont += 1
        s += n
print('A soma dos {} valores solicitados é igual a {}'.format(cont, s))