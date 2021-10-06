from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo: '))
rad = radians(ang)
s = sin(rad)
c = cos(rad)
t = tan(rad)
print('O ângulo {}º possui seno = {:.2f}, cosseno = {:.2f} e tangente = {:.2f}.'.format(ang, s, c, t))