peso_cartas = [8, 9, 10, 1, 2, 3, 4, 0, 0, 0, 6, 5, 7]
partidas = int(input())
partidas_ganhas = [0, 0]

for i in range(partidas):
    placar = [0, 0]
    partida = input()
    partida = list(map(int, partida.split()))
    for j in range(3):
        if peso_cartas[(partida[j] - 1)] < peso_cartas[(partida[j + 3] - 1)]:
            placar[1] += 1
        else:
            placar[0] += 1
    if placar[0] < placar[1]:
        partidas_ganhas[1] += 1
    elif placar[0] > placar[1]:
        partidas_ganhas[0] += 1

print(f"{partidas_ganhas[0]} {partidas_ganhas[1]}")
