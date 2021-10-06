n = int(input('Digite um número inteiro de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 100
c = n // 100 % 1000
m = n // 1000 % 100
print('Unidades: {:2};'.format(u))
print('Dezenas:  {:2};'.format(d))
print('Centenas: {:2};'.format(c))
print('Milhares: {:2}.'.format(m))