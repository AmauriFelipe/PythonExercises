r1 = float(input('Digite o valor do primeiro segmento: '))
r2 = float(input('Digite o valor do segundo segmento: '))
r3 = float(input('Digite o valor do terceiro segmento: '))
if r1 <= r2 + r3 and r2 <= r1 + r3 and r3 <= r1 + r2:
    print('Esses três segmentos formam um triângulo.')
else:
    print('Esses três segmentos não formam um triângulo.')