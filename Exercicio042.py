s1 = float(input('Digite o valor do primeiro segmento: '))
s2 = float(input('Digite o valor do segundo segmento: '))
s3 = float(input('Digite o valor do terceiro segmento: '))
if s1 <= s2 + s3 and s2 <= s1 + s3 and s3 <= s1 + s2:
    print('Esses três segmentos \033[1;32mPODEM\033[m formar um triângulo.')
    print(' ')
    if s1 == s2 == s3:
        print('Esse é um triângulo \033[1;33mEQUILÁTERO\033[m.')
    elif s1 != s2 != s3:
        print('Esse é um triângulo \033[1;33mESCALENO\033[m.')
    else:
        print('Esse é um triângulo \033[1;33mISÓSCELES\033[m.')
else:
    print('Esses três segmentos \033[1;31mNÃO PODEM\033[m formar um triângulo.')