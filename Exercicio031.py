d = float(input('Qual a distância da viagem em quilômetros? '))
if d <= 200:
    print('O preço da passagem será R${:.2f}.'.format(d*0.5))
else:
    print('O preço da passagem será R${:.2f}.'.format(d*0.45))