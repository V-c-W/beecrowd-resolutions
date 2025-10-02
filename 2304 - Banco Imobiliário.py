valores = input()
dinheiro, operacoes = map(int, valores.split())

D, E, F = dinheiro, dinheiro, dinheiro

def compra(valor, pessoa):
    globals()[pessoa] -= int(valor)


def venda(valor, pessoa):
    globals()[pessoa] += int(valor)


def aluguel(valor, pessoa_um, pessoa_dois):
    globals()[pessoa_um] += int(valor)
    globals()[pessoa_dois] -= int(valor)


for i in range(operacoes):
    operacao = input()
    operacao = list(map(str, operacao.split()))
    if operacao[0] == 'C':
        compra(operacao[2], operacao[1])
    elif operacao[0] == 'V':
        venda(operacao[2], operacao[1])
    else:
        aluguel(operacao[3], operacao[1], operacao[2])

print(f"{D} {E} {F}")
