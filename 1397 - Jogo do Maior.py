while True:
    i = int(input())
    if i == 0:
        break
    pontos_jum, pontos_jdois = 0, 0
    for j in range(i):
        jogo = input()
        jogador_um, jogador_dois = map(int, jogo.split())
        if jogador_um > jogador_dois:
            pontos_jum += 1
        elif jogador_dois > jogador_um:
            pontos_jdois += 1
        else:
            pass
    print(f"{pontos_jum} {pontos_jdois}")
