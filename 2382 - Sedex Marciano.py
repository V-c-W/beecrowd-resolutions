import math

dados = input()
dados = list(map(int, dados.split()))
possivel = 'S'

diag = math.sqrt(dados[0]**2 + dados[1]**2 + dados[2]**2)
diam = 2 * dados[3]

if not diag <= diam:
    possivel = 'N'

print(possivel)
