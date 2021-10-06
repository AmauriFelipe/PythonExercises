dias = int(input('Escreva o número de dias em que o carro esteve alugado: '))
km = float(input('Escreva a distância percorrida em quilômetros: '))
vd = dias * 60
vkm = km * 0.15
vt = vd + vkm
print('O preço total a pagar é R${:.2f}, considerando que custou R$60 por dia e R$0,15 por quilômetro rodado.'.format(vt))