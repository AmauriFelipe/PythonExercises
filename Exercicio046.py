from time import sleep
print('Contagem regressiva pros fogos de artifício: ')
for c in range(10, 0, -1):
    sleep(1)
    print(c)
print('Foi.')