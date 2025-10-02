casos = int(input())

for i in range(casos):
    lista_instrucoes = []
    num_instrucoes = int(input())
    posicao = 0
    for j in range(num_instrucoes):
        instrucao = input()
        lista_instrucoes.append(instrucao)
        if instrucao == 'LEFT':
            posicao -= 1
        elif instrucao == 'RIGHT':
            posicao += 1
        else:
            instrucao = list(map(str, instrucao.split()))
            instrucao = int(instrucao[2])
            lista_instrucoes[-1] = lista_instrucoes[instrucao - 1]
            if lista_instrucoes[-1] == 'LEFT':
                posicao -= 1
            elif lista_instrucoes[-1] == 'RIGHT':
                posicao += 1
    print(posicao)
