peso = float(input('Digite seu peso em quilos: '))
altura = float(input('Digite sua altura em centímetros: '))
imc = peso / (altura / 100) ** 2
print('Seu IMC (Índice de Massa Corporal) é \033[1;33m{:.2f}\033[m.'.format(imc))
if imc <= 18.5:
    print('\033[1;31mVocê está abaixo do peso.\033[m')
elif 18.5 < imc < 25:
    print('\033[1;32mVocê está no peso ideal.\033[m')
elif 25 <= imc < 30:
    print('\033[1;33mVocê está com sobrepeso.\033[m')
elif 30 <= imc < 40:
    print('\033[1;31mVocê está com obesidade.\033[m')
elif 40 <= imc:
    print('\033[1;31mVocê está com obesidade mórbida.\033[m')