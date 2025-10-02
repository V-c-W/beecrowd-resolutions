'''
Considerando que uma escada de 5 pilhas de pedra precisa de no minimo 5+4+3+2+1 blocos
ou (5+1 * 2) + (5+1 / 2), podemos dizer que para N pilhas, temos:
(N + 1) * ((N - 1) / 2) + ((N + 1) / 2) para N impar
(N + 1) * (N / 2) para N par
Logo, se temos X blocos, podemos subtrair de X esse valor minimo encontrado para N pilhas
(X - {blocos N pilhas} = M) depois fazer M mod N para saber se e possivel fazer uma escada.
Sendo possivel, podemos descobrir quantas pedras precisamos mover, precisamos apenas
subtrair cada pilha atual pela pilha da escada final, no final teremos numeros positivos e
negativos que somados resultam 0, logo precisamos apenas da soma dos positivos para saber
quantas pedras precisam ser movidas.
'''

pilhas = int(input())
pedras_por_pilha = list(map(int, input().split(" ")))

if pilhas % 2 == 0:
    minimo = (pilhas + 1) * (pilhas / 2)
    pedras_extras = sum(pedras_por_pilha) - minimo
    if pedras_extras % pilhas != 0:
        print("-1")
    else:
        pedras_extras = pedras_extras / pilhas
        escada_final = [i + pedras_extras for i in range(1, pilhas + 1)]
        pedras_movidas = [x - y for x,y in zip(pedras_por_pilha, escada_final)]
        print(int(sum([i for i in pedras_movidas if i >= 0])))
else:
    minimo = (pilhas + 1) * ((pilhas - 1) / 2) + ((pilhas + 1) / 2)
    pedras_extras = sum(pedras_por_pilha) - minimo
    if pedras_extras % pilhas != 0:
        print("-1")
    else:
        pedras_extras = pedras_extras / pilhas
        escada_final = [i + pedras_extras for i in range(1, pilhas + 1)]
        pedras_movidas = [x - y for x,y in zip(pedras_por_pilha, escada_final)]
        print(int(sum([i for i in pedras_movidas if i >= 0])))
