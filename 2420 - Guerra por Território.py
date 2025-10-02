num_terri = int(input())
territorios = input()
territorios = list(map(int, territorios.split()))
divisao = sum(territorios) / 2
soma = 0

for i in range(num_terri):
    soma += territorios[i]
    if soma == divisao:
        print(i+1)
        break
