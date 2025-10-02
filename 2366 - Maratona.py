prova = 'S'
dados = input()
postos, distancia_max = map(int, dados.split())
distancias = input()
distancias = list(map(int, distancias.split()))


for i in range(postos - 1):
    if distancias[i + 1] - distancias[i] > distancia_max:
        prova = 'N'
        break
if 42195 - distancias[-1] > distancia_max:
    prova = 'N'

print(prova)
