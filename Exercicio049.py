n = int(input('Digite um número inteiro para ver sua tabuada: '))
print(' ')
for tab in range(1, 10+1):
    print('{} x {:2} = {}'.format(n, tab, n*tab))