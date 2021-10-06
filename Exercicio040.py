nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2)/2
print(' ')
print('Sua média é {}.'.format(media))
if media < 5:
    print('Você está \033[1;31mREPROVADO\033[m.')
elif 5 < media < 6.9:
    print('Você está em \033[1;33mRECUPERAÇÃO\033[m.')
else:
    print('Você está \033[1;32mAPROVADO\033[m.')