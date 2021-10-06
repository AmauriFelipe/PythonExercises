s = float(input('Escreva o salário: '))
if s>1250:
    print('O aumento será de 10% e o salário final será R${:.2f}.'.format(s*1.1))
else:
    print('O aumento será de 15% e o salário final será R${:.2f}.'.format(s*1.15))