H=float(input('Digite a altura da parede em metros: '))
x=float(input('Digite o comprimento da base da parede em metros: '))
A=H*x
l=A/2
print('A área dessa parede é {}m² (metros quadrados)'.format(A))
print('e o volume de tinta gasto pra pintá-la é {} litros (considerando q cada litro pinta 2m²)'.format(l))