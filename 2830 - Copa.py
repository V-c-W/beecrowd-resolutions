kung = int(input())
lu = int(input())
chave = [0] * 16
chave[kung-1] = 1
chave[lu-1] = 1
chave_seguinte = []
pos = 0
fase = ['oitavas', 'quartas', 'semifinal']

if kung > 8 and lu <= 8 or kung <= 8 and lu > 8:
    print('final')
else:
    while True:
        for i in range(0, len(chave), 2):
            chave_seguinte.append(chave[i] + chave[i+1])
        chave = chave_seguinte
        chave_seguinte = []
        if max(chave) == 2:
            break
        pos += 1
    print(fase[pos])
