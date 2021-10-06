import math
b = float(input('Digite o valor do cateto oposto: '))
c = float(input('digite o valor do cateto adjacente: '))
a = math.hypot(b, c)
print('No triângulo retângulo de catetos {} e {} a hipotenusa mede {}.'.format(b, c, a))