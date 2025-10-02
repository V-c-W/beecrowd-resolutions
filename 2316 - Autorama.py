def autorama_ranking(K, N, M, sensores):
    carro_pos = {i: 0 for i in range(1, N + 1)}
    carro_tempo = {i: 0 for i in range(1, N + 1)}
    checagens = {i: 1 for i in range(1, N + 1)}

    for tempo, (carro, checagem) in enumerate(sensores):
        if checagem == checagens[carro]:
            carro_pos[carro] += 1
            checagens[carro] = (checagens[carro] % K) + 1
            carro_tempo[carro] = tempo

    sorted_carros = sorted(range(1, N + 1), key=lambda x: (-carro_pos[x], carro_tempo[x]))

    return sorted_carros

K, N, M = map(int, input().split())
sensores = [tuple(map(int, input().split())) for _ in range(M)]

ranking = autorama_ranking(K, N, M, sensores)

print(" ".join(map(str, ranking)))
