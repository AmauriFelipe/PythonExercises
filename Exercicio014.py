C = float(input('Escreva uma temperatura em graus celsius: '))
F = C * 1.8 + 32
K = C + 273
print('A temperatura {}ºC (Celsius) equivale a {:.3f}ºF (Farnheit) e {}K (Kelvin).'.format(C, F, K))