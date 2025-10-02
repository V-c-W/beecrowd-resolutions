casos = int(input())

for i in range(casos):
    valores = input()
    valor_um, valor_dois = map(str, valores.split())
    if int(valor_um) < int(valor_dois):
        print('nao encaixa')
    elif valor_um[(len(valor_um) - len(valor_dois)):] == valor_dois:
        print('encaixa')
    else:
        print('nao encaixa')
