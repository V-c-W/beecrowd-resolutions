dados = input()
pinos, altura = map(int, dados.split())
dados = input()
dados = list(map(int, dados.split()))
i = 0
movimentos = 0
movimentos_total = 0

while True:
    if i >= pinos:
        break
    if dados[i] == altura:
        i += 1
        continue
    if altura - dados[i] < 0:
        movimentos = altura - dados[i]
        dados[i] += movimentos
        dados[i + 1] += movimentos
        movimentos_total += (-1) * movimentos
    else:
        movimentos = altura - dados[i]
        dados[i] += movimentos
        dados[i + 1] += movimentos
        movimentos_total += movimentos

print(movimentos_total)
