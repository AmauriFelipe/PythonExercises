#Programa q lê o nome de uma cidade e diga se começa com "Santo"
cid = str(input('Escreva o nome de uma cidade: ')).strip().lower()
print(cid[:5] == 'santo')