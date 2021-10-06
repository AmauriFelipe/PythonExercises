from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = atual - nascimento
print(' ')
print('O atleta tem {} anos.'.format(idade))
print(' ')
if 0 < idade <= 9:
    print('Está na categoria \033[1;32mMIRIM\033[m de natação.')
elif 9 < idade <= 14:
    print('Está na categoria \033[1;32mINFANTIL\033[m de natação.')
elif 14 < idade <= 19:
    print('Está na categoria \033[1;32mJÚNIOR\033[m de natação.')
elif 19 < idade <= 20:
    print('Está na categoria \033[1;32mSÊNIOR\033[m de natação.')
else:
    print('Está na categoria \033[1;32mMASTER\033[m de natação.')