print('{:+^40}'.format(' LOJA COMPRE BEM '))
print(' ')
preco = float(input('Preço das compras: R$'))
print(' ')
print('''\033[1;32mFormas de pagamento:\033[m
[ 1 ] À vista em dinheiro/cheque: 10% de desconto;
[ 2 ] À vista no cartão: 5% de desconto;
[ 3 ] Em até 2x: preço formal;
[ 4 ] 3x ou mais no cartão: 20% de juros.''')
print(' ')
pag = int(input('Sua escolha de pagamento: '))
print(' ')
if pag == 1:
    total = preco * 0.9
    print('Sua compra em dinheiro ou cheque terá 10% de desconto.')
elif pag == 2:
    total = preco * 0.95
    print('Sua compra será à vista no cartão e terá 5% de desconto.')
elif pag == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}.'.format(parcela))
elif pag == 4:
    total = preco * 1.2
    parcela = int(input('Em quantas parcelas? '))
    totparc = total / parcela
    print('Sua compra será em {} parcelas de R${:.2f} no cartão com 20% de juros.'.format(parcela, totparc))
else:
    total = 0
    print('Essa escolha não é válida. Tente novamente.')
print('Sua compra de R${:.2f} vai ficar por \033[1;32mR${:.2f}\033[m no final.'.format(preco, total))