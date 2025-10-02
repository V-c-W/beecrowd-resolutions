mensagem = input()
crib = input()
possiveis = 0

for i in range(len(mensagem)-len(crib) + 1):
    possivel = True
    for j in range(len(crib)):
        if crib[j] == mensagem[j+i]:
            possivel = False
            break
    if possivel:
        possiveis += 1

print(possiveis)
