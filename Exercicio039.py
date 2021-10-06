from datetime import date
atual = date.today().year
nascimento = int(input('Digite o seu ano de nascimento: '))
idade = atual - nascimento
print(' ')
print('Quem nasceu em {} vai completar {} anos em {}.'.format(nascimento, idade, atual))
print(' ')
if idade < 18:
    print('Você ainda irá se alistar no exército.')
    if 18 - idade == 1:
        print('Falta 1 ano pra você se alistar.')
    else:
        print('Faltam {} anos pra você se alistar.'.format(18-idade))
elif idade == 18:
    print('Você deve se alistar no exército esse ano')
else:
    print('Você já passou do tempo de alistamento.')
    if idade - 18 == 1:
        print('Já se passou 1 ano.')
    else:
        print('Já se passaram {} anos.'.format(idade-18))