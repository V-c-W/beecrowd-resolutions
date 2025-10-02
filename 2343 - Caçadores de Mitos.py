raios_mesmo_lugar = 0
mapa = 501
coordenadas = [[0] * mapa for x in range(mapa)]
numero_raios = input()
for i in range(0, int(numero_raios)):
    x, y = input().split(" ")
    if coordenadas[int(x)][int(y)] != 0:
        raios_mesmo_lugar = 1
        break
    else:
        coordenadas[int(x)][int(y)] = 1
        
print(raios_mesmo_lugar)