soma = 0
cont = 0
for c in range(1, 6+1):
    n = int(input('Digite o {}º valor inteiro: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} números pares e a soma dos valores é {}.'.format(cont, soma))
