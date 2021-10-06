v = float(input('Escreva a velocidade do carro: '))
multa = (v - 80) * 7
if v <= 80:
    print(' ')
    print('Esse carro está dentro do limite de velocidade.')
else:
    print('Esse carro está acima do limite de velocidade.')
    print(' ')
    print('Deverá pagar R${:.2f} de multa.'.format(multa))