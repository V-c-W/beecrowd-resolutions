andar_um = int(input())
andar_dois = int(input())
andar_tres = int(input())

posicao_maquina = [0, 0, 0]

posicao_maquina[0] = (2 * andar_dois) + (4 * andar_tres)
posicao_maquina[1] = (2 * andar_um) + (2 * andar_tres)
posicao_maquina[2] = (2 * andar_dois) + (4 * andar_um)

print(min(posicao_maquina))
