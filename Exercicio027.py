#Programa que lê o nome de uma pessoa, mostrando o primeiro nome e o último nome separadamente.
nome = str(input('Escreva um nome completo: ')).strip()
separa = nome.split()
print('O primeiro nome é {} e o último é {}.'.format(separa[0], separa[len(separa)-1]))