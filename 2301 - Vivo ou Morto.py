teste = 1
while True:
    zeros = 0
    dados = input()
    num_participantes, rodadas = map(int, dados.split())
    if num_participantes == 0 and rodadas == 0:
        break
    eliminados = []
    participantes = input()
    participantes = list(map(int, participantes.split()))
    
    for i in range(rodadas):
        dados = input()
        dados = list(map(int, dados.split()))
        for j in range(dados[0]):
            if dados[j + 2] != dados[1]:
                participantes[j] = 0
        participantes = list(filter(lambda num: num != 0, participantes))

    print(f"Teste {teste}")
    print(f'{participantes[0]}')
    print("")
    teste += 1
